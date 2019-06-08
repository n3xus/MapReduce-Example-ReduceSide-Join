#!/usr/bin/python3
"""
Reduce Side Join Example
"""
import sys


def category_mapper():
    """ Maps videos to category
    Author Input format: video_id , Author Name

    Video Input format: video_id, trending_date, category_id, category, publish_time, views,likes, dislikes,
                        comment_count, ratings_disabled, video_error_or_removed, country

    Output format: video_id \t Author Name \t trending_date \t likes
    """
    for line in sys.stdin:
        author = "-"
        likes = "-"
        trending_date = "-"

        parts = line.strip().split(",")

        if len(parts) == 12:
            video_id = parts[0]
            trending_date = parts[1]
            likes = parts[6]
        else:
            video_id = parts[0]
            author = parts[1]

        if video_id == "video_id":
            continue

        print("{}\t{}\t{}\t{}".format(video_id, author, trending_date, likes))


if __name__ == "__main__":
    category_mapper()
