import json
import re
import struct


class Time(dict):
    def __init__(self, secs, nsecs):
        secs_over = int(nsecs) // 1e9
        self._secs = int(secs) + secs_over
        self._nsecs = int(nsecs) - secs_over * 1e9
        # enable json serialization
        dict.__init__(self, secs=self._secs, nsecs=self._nsecs)

    def to_nsec(self):
        return self._secs * int(1e9) + self._nsecs

    def __str__(self):
        return "%d" % self.to_nsec()


def read_sized(f):
    s = read_uint32(f)
    return f.read(s)


def pack_uint8(v): return struct.pack('<B', v)
def pack_uint32(v): return struct.pack('<L', v)
def pack_uint64(v): return struct.pack('<Q', v)
def pack_time(v): return pack_uint32(v.secs) + pack_uint32(v.nsecs)


def read_byte(f): return unpack_byte(f.read(1))
def read_bool(f): return bool(unpack_bool(f.read(1)))  # True or False
def read_uint8(f): return unpack_uint8(f.read(1))
def read_int8(f): return unpack_int8(f.read(1))
def read_uint16(f): return unpack_uint16(f.read(2))
def read_int16(f): return unpack_int16(f.read(2))
def read_uint32(f): return unpack_uint32(f.read(4))
def read_int32(f): return unpack_int32(f.read(4))
def read_uint64(f): return unpack_uint64(f.read(8))
def read_int64(f): return unpack_int64(f.read(8))
def read_float32(f): return unpack_float32(f.read(4))
def read_float64(f): return unpack_float64(f.read(8))
def read_time(f): return Time(*unpack_time(f.read(8)))


def unpack_arr(f, byte_len, arr_len, unpack_func):
    total_len = byte_len * arr_len
    v = f.read(total_len)
    return [unpack_func(v[i: i + byte_len]) for i in range(0, total_len, byte_len)]


# def read_uint8_arr(f, arr_len): return unpack_arr(f, 1, arr_len, unpack_uint8)
def read_uint8_arr(f, arr_len): return f.read(arr_len)


# def read_int8_arr(f, arr_len): return unpack_arr(f, 1, arr_len, unpack_int8)
def read_int8_arr(f, arr_len): return f.read(arr_len)


def read_uint16_arr(f, arr_len): return unpack_arr(
    f, 2, arr_len, unpack_uint16)


def read_int16_arr(f, arr_len): return unpack_arr(f, 2, arr_len, unpack_int16)


def read_uint32_arr(f, arr_len): return unpack_arr(
    f, 4, arr_len, unpack_uint32)


def read_int32_arr(f, arr_len): return unpack_arr(f, 4, arr_len, unpack_int32)


def read_uint64_arr(f, arr_len): return unpack_arr(
    f, 8, arr_len, unpack_uint64)


def read_int64_arr(f, arr_len): return unpack_arr(f, 8, arr_len, unpack_int64)


def read_float32_arr(f, length): return unpack_arr(
    f, 4, length, unpack_float32)


def read_float64_arr(f, length): return unpack_arr(
    f, 8, length, unpack_float64)


# to support non-utf8 decoding ex. /hdmap/horizon/map_offline
def decode(s):
    try:
        return s.decode('utf-8')
    except UnicodeDecodeError as e:
        return s.hex()


def read_string(f):
    s = read_sized(f)
    return decode(s)


def decode_str(v): return v if type(v) is str else v.decode()


def unpack_byte(v): return struct.unpack('<b', v)[0]
def unpack_bool(v): return struct.unpack('<B', v)[0]
def unpack_uint8(v): return struct.unpack('<B', v)[0]
def unpack_int8(v): return struct.unpack('<b', v)[0]
def unpack_uint16(v): return struct.unpack('<H', v)[0]
def unpack_int16(v): return struct.unpack('<h', v)[0]
def unpack_uint32(v): return struct.unpack('<L', v)[0]
def unpack_int32(v): return struct.unpack('<l', v)[0]
def unpack_uint64(v): return struct.unpack('<Q', v)[0]
def unpack_int64(v): return struct.unpack('<q', v)[0]
def unpack_float32(v): return struct.unpack('<f', v)[0]
def unpack_float64(v): return struct.unpack('<d', v)[0]
def unpack_time(v): return struct.unpack('<LL', v)


def strip_comments(text): return text.split("#")[0].strip()


def is_valid_package_resource_name(name):
    # http://wiki.ros.org/Names 1.2
    m = re.match(r'[a-zA-Z][0-9a-zA-Z_\/]*(\[\])?', name)
    if m is None or m[0] != name:
        return False
    if name.count("/") > 1:
        return False
    return True


class BytesEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return decode(obj)
        return json.JSONEncoder.default(self, obj)
