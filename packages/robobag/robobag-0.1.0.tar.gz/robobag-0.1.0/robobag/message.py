# import genpy.dynamic
import json
import os
import shutil
import sys
import tempfile
from io import BytesIO as StringIO

import av
import cv2
import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq
from tqdm import tqdm

from . import profile_pb2
from .util import (BytesEncoder, is_valid_package_resource_name, read_bool,
                   read_byte, read_float32, read_float32_arr, read_float64,
                   read_float64_arr, read_int8, read_int8_arr, read_int16,
                   read_int16_arr, read_int32, read_int32_arr, read_int64,
                   read_int64_arr, read_sized, read_string, read_time,
                   read_uint8, read_uint8_arr, read_uint16, read_uint16_arr,
                   read_uint32, read_uint32_arr, read_uint64, read_uint64_arr,
                   strip_comments)


class Field():
    # http://wiki.ros.org/msg 2.1

    def __init__(self, text):
        field_type, self._name = strip_comments(text).split(
            None, 1)  # use multi whitespace as sep

        self._package = None
        self._message_type = field_type
        self._is_arr = False
        self._arr_len = None

        # handle array type
        if '[' in field_type:
            self._is_arr = True
            if field_type.endswith("[]"):
                self._message_type = field_type[:-2]
            else:
                s = field_type.split("[")
                self._arr_len = int(s[1][:-1])
                self._message_type = s[0]

        # http://wiki.ros.org/Names 1.2
        if '/' in self._message_type:
            self._package, self._message_type = self._message_type.split('/')

        if not is_valid_package_resource_name(self.field_type):
            raise Exception("invalid field type name '%s'" % self.field_type)

    @property
    def name(self):
        return self._name

    @property
    def field_type(self):
        if self._package is None:
            return self._message_type
        else:
            return self._package + "/" + self._message_type

    @property
    def package(self):
        return self._package

    def __repr__(self):
        return "%s,%s,%s,%s" % (self._message_type, self._is_arr, self._arr_len, self._name)

    def parse_data(self, data_io):
        _read_type = {
            'byte': read_byte,
            'bool': read_bool,
            'uint8': read_uint8,
            'int8': read_int8,
            'uint16': read_uint16,
            'int16': read_int16,
            'uint32': read_uint32,
            'int32': read_int32,
            'uint64': read_uint64,
            'int64': read_int64,
            'float32': read_float32,
            'float64': read_float64,
            'time': read_time,
            'duration': read_time,
            'string': read_string
        }

        if self._message_type in _read_type:
            func = _read_type[self._message_type]
            rst = func(data_io)
            return rst

        raise Exception(
            "no read function for field type %s" % (self._message_type))

    def parse_arr_data(self, data_io, length):
        _read_arr = {
            'uint8': read_uint8_arr,
            'int8': read_int8_arr,
            'uint16': read_uint16_arr,
            'int16': read_int16_arr,
            'uint32': read_uint32_arr,
            'int32': read_int32_arr,
            'uint64': read_uint64_arr,
            'int64': read_int64_arr,
            'float32': read_float32_arr,
            'float64': read_float64_arr,
        }
        if self._message_type in _read_arr:
            func = _read_arr[self._message_type]
            rst = func(data_io, length)
            return rst
        else:
            raise Exception(
                "no read function for field type %s" % (self._message_type))

    def build_pa_field(self):
        _data_type = {
            'byte': pa.int8(),
            'bool': pa.bool_(),
            'uint8': pa.uint8(),
            'int8': pa.int8(),
            'uint16': pa.uint16(),
            'int16': pa.int16(),
            'uint32': pa.uint32(),
            'int32': pa.int32(),
            'uint64': pa.uint64(),
            'int64': pa.int64(),
            'float32': pa.float32(),
            'float64': pa.float64(),
            'time': pa.struct([("secs", pa.int64()), ('nsecs', pa.int64())]),
            'duration': pa.struct([("secs", pa.int64()), ('nsecs', pa.int64())]),
            'string': pa.string()
        }
        if self._message_type in _data_type:
            ty = _data_type[self._message_type]
            return ty
        raise Exception(
            "no parquet schema for field type %s" % (self._message_type))


class Constant():
    # http://wiki.ros.org/msg 2.2

    # TODO: incorporate const value
    def __init__(self, text):
        self._type, nv = strip_comments(text).split(" ", 1)
        self._name, self._value = nv.split("=")

    def __repr__(self):
        return "%s,%s,%s" % (self._type, self._name, self._value)


class Description():
    # http://wiki.ros.org/msg 2

    def __init__(self, field_type, text):
        self._text = text
        self._message_type = field_type
        self._package = None
        if '/' in self._message_type:
            self._package, self._message_type = field_type.split('/')

        self._fields = []
        self._constants = []
        self._has_header = False

        # parse text to get fields and constants
        for line in self._text.split("\n"):
            clean_line = strip_comments(line)
            if not clean_line:
                continue
            elif "=" in clean_line:
                self._constants.append(Constant(clean_line))
            else:
                if clean_line == "Header header":
                    self._has_header = True
                self._fields.append(Field(clean_line))

        self._schema = {}

    def parse_message(self, message_data_io, dep):
        data = {}
        message_type_arr = ['uint8', 'int8', 'uint16', 'int16',
                            'uint32', 'int32', 'uint64', 'int64', 'float32', 'float64']
        for field in self._fields:
            value = None
            if field._is_arr:
                value = []
                # 如果是为空，则说明是可变长度
                if field._arr_len is None:
                    length = read_uint32(message_data_io)
                else:
                    length = field._arr_len

                if field._message_type in message_type_arr:
                    # 如果是数组类型的，length大于0则执行解析，如果没有值的话，则跳过
                    if length > 0:
                        value = self._parse_field(
                            field, message_data_io, dep, length)
                else:
                    # 如果不是上面指定的数值类型的，则直接遍历获取
                    for i in range(length):
                        v = self._parse_field(
                            field, message_data_io, dep, 0)
                        value.append(v)
            else:
                value = self._parse_field(
                    field, message_data_io, dep, 0)

            data[field.name] = value

        return data

    def _parse_field(self, field, message_data_io, dep, length):
        ft = field.field_type
        # case 1 field type has package name
        if ft in dep:
            return dep[ft].parse_message(message_data_io, dep)

        # case 2 field type is header
        if ft == "Header" and "std_msgs/Header" in dep:
            return dep["std_msgs/Header"].parse_message(message_data_io, dep)

        # case 3 field type has no package name
        # concat package name to search in dep
        if field.package is None and self._package is not None:
            ft = self._package + "/" + ft
            if ft in dep:
                return dep[ft].parse_message(message_data_io, dep)

        # case 4
        # 如果length大于0则说明是数组
        if length == 0:
            # case 4
            return field.parse_data(message_data_io)
        else:
            return field.parse_arr_data(message_data_io, length)

    def build_pa_schema(self, dep):
        ty = []
        for field in self._fields:
            t = self._build_pa_field(field, dep)
            if field._is_arr:
                if field._arr_len is None:
                    t = pa.list_(t)
                else:
                    t = pa.list_(t, field._arr_len)

            ty.append(pa.field(field.name, t))

        return pa.struct(ty)

    def _build_pa_field(self, field, dep):
        ft = field.field_type
        if ft in dep:
            return dep[ft].build_pa_schema(dep)
        if ft == "Header" and "std_msgs/Header" in dep:
            return dep["std_msgs/Header"].build_pa_schema(dep)

        if field.package is None and self._package is not None:
            ft = self._package + "/" + ft
            if ft in dep:
                return dep[ft].build_pa_schema(dep)
        return field.build_pa_field()


class Registry():
    def __init__(self, core_type, text):
        self._core_type = core_type
        self._text = text

        msg_texts = text.split('\n'+'='*80+'\n')
        self._core_msg = Description(core_type, msg_texts[0])

        self._dep_msg = {}
        for msg_text in msg_texts[1:]:
            msg_line, dep_text = msg_text.split("\n", 1)
            if not msg_line.startswith("MSG:"):
                raise Exception()
            dep_type = msg_line[5:].strip()
            self._dep_msg[dep_type] = Description(dep_type, dep_text)

    def parse_message(self, message_bytes):
        message_data_io = StringIO(message_bytes)
        return self._core_msg.parse_message(message_data_io, self._dep_msg)

    def build_schema(self):
        fields = self._core_msg.build_pa_schema(self._dep_msg)
        # bag topic type name ex. "sensor_msgs/CompressedImage" is not valid in hive, use replacement
        column_name = self._core_type.replace("/", "_")
        return pa.schema(pa.struct([pa.field(column_name, fields)]))

class Message():
    def __init__(self, bag_file_obj, profile_obj, show_progress=False):
        self._file = bag_file_obj
        self._profile = profile_pb2.Profile()
        self._profile.ParseFromString(profile_obj.read())
        self._show_progress = show_progress

        self._conns = {}
        self._topics = {}
        for c in self._profile.connection:
            if c.conn not in self._conns:
                self._conns[c.conn] = c
                self._topics[c.topic] = c

    @property
    def topics(self):
        return list(self._topics.keys())

    def read_message_header(self, topic):
        header = []
        for c in self._profile.chunk:
            for md in c.message_data:
                conn = md.conn
                if self._conns[conn].topic == topic:
                    header.append(md)
        return header

    def read_message(self, topic):
        message_data_index = []
        for c in self._profile.chunk:
            for md in c.message_data:
                conn = md.conn
                if self._conns[conn].topic == topic:
                    message_data_index.append(md)

        t = self._topics[topic]

        registry = Registry(t.type, t.message_definition)
        pa_schema = registry.build_schema()
        hive_schema = self._to_hive_schema(pa_schema)

        data = []
        it = message_data_index
        if self._show_progress:
            it = tqdm(message_data_index, desc=f"read {topic} data")

        for idx in it:
            self._file.seek(idx._start)
            header = read_sized(self._file)
            message_bytes = read_sized(self._file)
            d = registry.parse_message(message_bytes)
            data.append(d)
        return [data], pa_schema, hive_schema

    def _to_hive_schema(self, pa_schema):
        def to_hive_type(t):
            if pa.types.is_boolean(t):
                return "BOOLEAN"
            elif pa.types.is_int8(t):
                return "TINYINT"
            elif pa.types.is_int16(t):
                return "SMALLINT"
            elif pa.types.is_int32(t):
                return "INT"
            elif pa.types.is_int64(t):
                return "BIGINT"
            elif pa.types.is_uint8(t):
                return "SMALLINT"  # unsign not unsupported in spark
            elif pa.types.is_uint16(t):
                return "INT"  # unsign not unsupported in spark
            elif pa.types.is_uint32(t):
                return "BIGINT"  # unsign not unsupported in spark
            elif pa.types.is_uint64(t):
                return "BIGINT"  # unsign not unsupported in spark
            elif pa.types.is_float32(t):
                return "FLOAT"
            elif pa.types.is_float64(t):
                return "DOUBLE"
            elif pa.types.is_string(t):
                return "STRING"
            elif pa.types.is_list(t) or pa.types.is_fixed_size_list(t):
                item = to_hive_type(t.value_type)
                return "ARRAY<{}>".format(item)
            elif pa.types.is_struct(t):
                fields = []
                for field in t:
                    f = "`{}`: {}".format(field.name, to_hive_type(field.type))
                    fields.append(f)
                return "STRUCT<{}>".format(", ".join(fields))
            else:
                raise Exception("no hive type for {}".format(t))
        fields = []
        for name, _type in zip(pa_schema.names, pa_schema.types):
            c = "`{}` {}".format(name, to_hive_type(_type))
            fields.append(c)
        return ", ".join(fields)

    def save_parquet(self, data, pa_schema, parquet_file_obj):
        table = pa.Table.from_arrays(data, schema=pa_schema)
        pq.write_table(table, parquet_file_obj,
                       compression="snappy", flavor='spark')

    def save_mp4(self, data, mp4_file_path):
        d = data[0]

        d.sort(key=lambda i: i['header']['stamp']["secs"] *
               1e9 + i['header']['stamp']["nsecs"])

        format = d[0]['format']
        if format != 'jpeg':
            raise Exception(f"format {format} to mp4 not supported")

        # cal fps 
        start = 0
        total_interval = 0
        num_interval = 0
        for i in d:
            end = i['header']['stamp']["secs"] * \
                1e9 + i['header']['stamp']["nsecs"]
            interval = end / 1e9 - start / 1e9
            if start != 0 and interval < 1:
                num_interval += 1
                total_interval = total_interval + interval
            start = end
        avg_interval = total_interval/num_interval
        fps = int(round(1/avg_interval))

        img_buffers = [np.asarray(
            bytearray(i['data']), dtype=np.uint8) for i in d]

        # cal width & height
        with tempfile.NamedTemporaryFile(suffix="."+format) as tmp:
            tmp.write(img_buffers[0])
            img = cv2.imread(tmp.name)
            img_height, img_width, _ = img.shape

        # write
        video = cv2.VideoWriter(mp4_file_path,
                                cv2.VideoWriter_fourcc(*'mp4v'),
                                fps, (img_width, img_height))
        it = img_buffers
        if self._show_progress:
            it = tqdm(it, desc="save image frames")
        for buf in it:
            with tempfile.NamedTemporaryFile(suffix="."+format) as tmp:
                tmp.write(buf)
                img = cv2.imread(tmp.name)
                video.write(img)

        video.release()

    def save_jpeg_seq(self, data, jpeg_file_dir):
        d = data[0]

        d.sort(key=lambda i: i['header']['stamp']["secs"] *
               1e9 + i['header']['stamp']["nsecs"])

        format = d[0]['format']

        if format == 'jpeg':
            for msg in d:
                sec = int(msg['header']['stamp']["secs"])
                nsec = int(msg['header']['stamp']["nsecs"])
                ts = '{}.{:09d}'.format(sec, nsec)
                img_path = "%s/%s.jpeg" % (jpeg_file_dir, ts)
                with open(img_path, "wb") as o:
                    o.write(msg['data'])

        elif format == 'h264':
            tmp_dir = jpeg_file_dir+"/temp"
            os.mkdir(tmp_dir)

            frame_ts = []
            h264_file = None
            outs = []
            for msg in d:
                sec = int(msg['header']['stamp']["secs"])
                nsec = int(msg['header']['stamp']["nsecs"])
                ts = '{}.{:09d}'.format(sec, nsec)
                msg_bytes = bytes(bytearray(msg['data']))
                buf = StringIO(msg_bytes)

                is_i = False
                buf.seek(0)
                while True:
                    cur = buf.tell()
                    b = buf.read(4)
                    if b == b'':
                        break
                    elif b == b'\x00\x00\x00\x01':
                        header = buf.read(1)
                        header_binary = int.from_bytes(
                            header, byteorder=sys.byteorder)
                        nut = int(bin(header_binary)[-5:], 2)
                        if nut == 5:
                            is_i = True
                            break
                        if nut == 1:
                            break
                    buf.seek(cur+1)

                if is_i:
                    if h264_file is not None:
                        h264_file.close()
                        outs.append(h264_file.name)
                    h264_file = open(f"{tmp_dir}/{ts}.h264", 'wb')
                    h264_file.write(msg_bytes)
                    frame_ts.append(ts)
                else:
                    if h264_file is not None:
                        h264_file.write(msg_bytes)
                        frame_ts.append(ts)
            if h264_file is not None:
                h264_file.close()
                outs.append(h264_file.name)

            i = 0
            it = outs
            if self._show_progress:
                it = tqdm(outs, desc="save jpeg sequence")
            for f in it:
                container = av.open(f)
                for frame in container.decode(video=0):
                    img_path = jpeg_file_dir+f"/{frame_ts[i]}.jpeg"
                    frame.to_image().save(img_path)
                    i = i+1
            shutil.rmtree(tmp_dir)
        else:
            raise Exception(f"format {format} not supported")

    def save_json(self, header, data, json_file_path):
        out = [{'time': {'secs': h.time.secs, 'nsecs': h.time.nsecs}, 'data': d}
               for h, d in zip(header, data[0])]
        with open(json_file_path, 'w') as o:
            json.dump(out, o, cls=BytesEncoder)

    def save_jsonl(self, header, data, jsonl_file_path):
        with open(jsonl_file_path, 'w') as o:
            for h, d in zip(header, data[0]):
                line = {'time': {'secs': h.time.secs,
                                 'nsecs': h.time.nsecs}, 'data': d}
                o.write(json.dumps(line,  cls=BytesEncoder) + "\n")
