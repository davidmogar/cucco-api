from flask import request

from app.api import common
from app.api.v1 import api
from app.common import functions
from app.common.analytics import track_event
from app.extensions import limiter

@api.route('/accents', methods=['GET', 'POST'])
@limiter.limit('30 per hour')
def accents():
    track_event('public', 'accents', request.method)

    return functions.remove_accent_marks(request)

@api.route('/characters', methods=['GET', 'POST'])
@limiter.limit('30 per hour')
def characters():
    track_event('public', 'characters', request.method)

    return functions.replace_characters(request)

@api.route('/emails', methods=['GET', 'POST'])
@limiter.limit('30 per hour')
def emails():
    track_event('public', 'emails', request.method)

    return functions.replace_emails(request)

@api.route('/emojis', methods=['GET', 'POST'])
@limiter.limit('30 per hour')
def emojis():
    track_event('public', 'emojis', request.method)

    return functions.replace_emojis(request)

@api.route('/hyphens', methods=['GET', 'POST'])
@limiter.limit('30 per hour')
def hyphens():
    track_event('public', 'hyphens', request.method)

    return functions.replace_hyphens(request)

@api.route('/normalize', methods=['GET', 'POST'])
@limiter.limit('10 per hour')
def normalize():
    track_event('public', 'normalize', request.method)

    return functions.normalize(request)

@api.route('/punctuation', methods=['GET', 'POST'])
@limiter.limit('30 per hour')
def punctuation():
    track_event('public', 'punctuation', request.method)

    return functions.replace_punctuation(request)

@api.route('/status', methods=['GET', 'POST'])
def status():
    return common.status()

@api.route('/stopwords', methods=['GET', 'POST'])
@limiter.limit('10 per hour')
def stopwords():
    track_event('public', 'stopwords', request.method)

    return functions.remove_stop_words(request)

@api.route('/symbols', methods=['GET', 'POST'])
@limiter.limit('30 per hour')
def symbols():
    track_event('public', 'symbols', request.method)

    return functions.replace_symbols(request)

@api.route('/urls', methods=['GET', 'POST'])
@limiter.limit('30 per hour')
def urls():
    track_event('public', 'urls', request.method)

    return functions.replace_urls(request)

@api.route('/whitespaces', methods=['GET', 'POST'])
@limiter.limit('30 per hour')
def whitespaces():
    track_event('public', 'whitespaces', request.method)

    return functions.remove_extra_whitespaces(request)
