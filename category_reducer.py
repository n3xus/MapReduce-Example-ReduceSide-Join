#!/usr/bin/python3
import sys


def read_map_output(file):
    for line in file:
        yield line.strip().split('\t')


def category_reducer():
    current_video_id = None
    current_author = None

    for video_id, author, trending_date, likes in read_map_output(sys.stdin):

        if not current_video_id or current_video_id != video_id:
            current_video_id = video_id
            current_author = author
        elif current_video_id == video_id:
            output = "{}\t{}\t{}\t{}".format(current_video_id, current_author, trending_date, likes)
            print(output)


if __name__ == "__main__":
    category_reducer()
