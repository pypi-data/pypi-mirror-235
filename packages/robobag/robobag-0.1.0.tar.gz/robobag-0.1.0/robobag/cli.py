import os
import shutil
from collections import Counter
from pathlib import Path

import click

from .bag import Bag
from .message import Message


@click.group()
@click.version_option()
def cli():
    pass


def profile_func(bag_file_path):
    bag_profile_path = bag_file_path.replace('.bag', 'pb.bin')
    if os.path.exists(bag_profile_path):
        return

    fp = Path(bag_file_path)
    with open(fp, "rb") as f:
        bag = Bag(file_obj=f, show_progress=True)

    with open(fp.with_suffix('.pb.bin'), 'wb') as o:
        o.write(bag.profile.SerializeToString())

    with open(fp.with_suffix('.yaml'), 'wb') as o:

        msg_count = Counter()
        for chunk in bag.profile_json['chunk']:
            for msg in chunk['message_data']:
                if msg['_op'] == 2:
                    msg_count[msg['conn']] += 1

        for index, conn in enumerate(bag.profile_json['connection']):
            if index != 0:
                o.write("\n\n\n\n".encode("utf-8"))
            title = "# conn = %s\n# type = %s\n# topic = %s\n# msg count = %s\n" % (
                conn['conn'], conn['type'], conn['topic'], msg_count[conn['conn']])
            o.write((title).encode("utf-8"))
            o.write(conn['message_definition'].encode('utf8'))


@click.command()
@click.option('bag_file_path', '-i', '--input', required=True, prompt="Input bag file path", type=click.Path(exists=True))
def profile(bag_file_path):
    profile_func(bag_file_path)

def extract_func(message, message_topic, message_format, fp_new):

    topic_data, topic_schema, hql = message.read_message(
        message_topic)
    topic_header = message.read_message_header(
        message_topic)

    if message_format == "parquet":
        with open(fp_new+".parquet", "wb") as o:
            message.save_parquet(topic_data, topic_schema, o)

        with open(fp_new+".hql", "w") as o:
            o.write(hql)

    elif message_format == "mp4":
        message.save_mp4(topic_data,
                         fp_new+".mp4")

    elif message_format == "jpeg_seq":
        dir_path = fp_new
        if os.path.exists(dir_path) and os.path.isdir(dir_path):
            shutil.rmtree(dir_path)
        os.mkdir(dir_path)
        message.save_jpeg_seq(topic_data, dir_path)

    elif message_format == "json":
        message.save_json(topic_header, topic_data, fp_new+'.json')

    elif message_format == "jsonl":
        message.save_jsonl(topic_header, topic_data, fp_new+'.jsonl')


@ click.command()
@ click.option('bag_file_path', '-i', '--input', required=True, prompt="Input bag file path", type=click.Path(exists=True))
@ click.option('message_topic', '-t', '--topic', required=True, prompt="Message topic", type=click.STRING)
@ click.option('message_format', '-f', '--format', required=True, prompt="Message format", type=click.Choice(['parquet', 'mp4', 'jpeg_seq', 'json', 'jsonl']))
def extract(bag_file_path, message_topic, message_format):
    bag_profile_path = bag_file_path.replace('.bag', '.pb.bin')
    if not os.path.exists(bag_profile_path):
        profile_func(bag_file_path)

    fp = Path(bag_file_path)
    fpp = Path(bag_profile_path)
    with open(fp, "rb") as f:
        with open(fpp, "rb") as p:
            message = Message(f, p, show_progress=True)
            topics = []
            if message_topic == '*':
                topics = message.topics
            elif message_topic in message.topics:
                topics.append(message_topic)

            for topic in topics:
                fp_new = fp.with_suffix("."+topic.replace("/", "_"))
                extract_func(message,
                             topic, message_format, str(fp_new))


cli.add_command(profile)
cli.add_command(extract)

if __name__ == '__main__':
    cli()
