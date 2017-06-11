from flask import Blueprint, request

from app.common import functions
from app.common.analytics import track_event
from app.extensions import limiter

public = Blueprint('public', __name__, url_prefix='/api/public')

@public.route('/accents', methods=['GET', 'POST'])
@limiter.limit('30 per hour')
def accents():
    track_event('public', 'accents', request.method)

    return functions.remove_accent_marks(request)

@public.route('/characters', methods=['GET', 'POST'])
@limiter.limit('30 per hour')
def characters():
    track_event('public', 'characters', request.method)

    return functions.replace_characters(request)

@public.route('/emails', methods=['GET', 'POST'])
@limiter.limit('30 per hour')
def emails():
    track_event('public', 'emails', request.method)

    return functions.replace_emails(request)

@public.route('/emojis', methods=['GET', 'POST'])
@limiter.limit('30 per hour')
def emojis():
    track_event('public', 'emojis', request.method)

    return functions.replace_emojis(request)

@public.route('/hyphens', methods=['GET', 'POST'])
@limiter.limit('30 per hour')
def hyphens():
    track_event('public', 'hyphens', request.method)

    return functions.replace_hyphens(request)

@public.route('/normalize', methods=['GET', 'POST'])
@limiter.limit('10 per hour')
def normalize():
    track_event('public', 'normalize', request.method)

    return functions.normalize(request)

@public.route('/punctuation', methods=['GET', 'POST'])
@limiter.limit('30 per hour')
def punctuation():
    track_event('public', 'punctuation', request.method)

    return functions.replace_punctuation(request)

@public.route('/stopwords', methods=['GET', 'POST'])
@limiter.limit('10 per hour')
def stopwords():
    track_event('public', 'stopwords', request.method)

    return functions.remove_stop_words(request)

@public.route('/symbols', methods=['GET', 'POST'])
@limiter.limit('30 per hour')
def symbols():
    track_event('public', 'symbols', request.method)

    return functions.replace_symbols(request)

@public.route('/urls', methods=['GET', 'POST'])
@limiter.limit('30 per hour')
def urls():
    track_event('public', 'urls', request.method)

    return functions.replace_urls(request)

@public.route('/whitespaces', methods=['GET', 'POST'])
@limiter.limit('30 per hour')
def whitespaces():
    track_event('public', 'whitespaces', request.method)

    return functions.remove_extra_whitespaces(request)
