from time import mktime
from datetime import datetime

from flask import Blueprint, Response, request, abort, current_app as app

import pytz
import feedparser

frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def index():
    if not request.args.get('feed'):
        abort(404)

    feed = feedparser.parse(request.args.get('feed'))

    if feed.bozo == 1:
        abort(500)

    tweets = []

    for entry in feed.entries:
        _timestamp = datetime.fromtimestamp(mktime(entry.published_parsed))
        timestamp = pytz.utc.localize(_timestamp).isoformat()

        tweets.append("{0}\t{1} - <{2}>\n".format(timestamp, entry.title,
                                                  entry.link))

    return Response(''.join(tweets), mimetype="text/plain")
