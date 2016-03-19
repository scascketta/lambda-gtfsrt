#!/usr/bin/env python
import json
import requests
from protobuf_to_dict import protobuf_to_dict
from google.transit import gtfs_realtime_pb2 as gtfsrt

DEFAULT_URL = 'https://data.texas.gov/download/eiei-9rpf/application/octet-stream'


def fetch_feed(url):
    feed = gtfsrt.FeedMessage()
    res = requests.get(url)
    feed.ParseFromString(res.content)
    return feed


def lambda_handler(event, ctx):
    url = event.get('url')

    if url:
        feed = fetch_feed(url)
        return json.dumps(protobuf_to_dict(feed))
    else:
        return {'error_message': 'Requires the `url` param'}


if __name__ == '__main__':
    print lambda_handler({'url': DEFAULT_URL}, None)
