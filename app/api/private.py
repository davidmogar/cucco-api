from flask import Blueprint, request
from flask_login import login_required

from app.api import common
from app.common import functions
from app.common.analytics import track_event
from app.extensions import limiter

private = Blueprint('private', __name__, url_prefix='/private')

@private.route('/accents', methods=['GET', 'POST'])
@login_required
def accents():
    track_event('private', 'accents', request.method)

    return functions.remove_accent_marks(request)

@private.route('/characters', methods=['GET', 'POST'])
@login_required
def characters():
    track_event('private', 'characters', request.method)

    return functions.replace_characters(request)

@private.route('/emails', methods=['GET', 'POST'])
@login_required
def emails():
    track_event('private', 'emails', request.method)

    return functions.replace_emails(request)

@private.route('/emojis', methods=['GET', 'POST'])
@login_required
def emojis():
    track_event('private', 'emojis', request.method)

    return functions.replace_emojis(request)

@private.route('/hyphens', methods=['GET', 'POST'])
@login_required
def hyphens():
    track_event('private', 'hyphens', request.method)

    return functions.replace_hyphens(request)

@private.route('/normalize', methods=['GET', 'POST'])
@login_required
def normalize():
    track_event('private', 'normalize', request.method)

    return functions.normalize(request)

@private.route('/punctuation', methods=['GET', 'POST'])
@login_required
def punctuation():
    track_event('private', 'punctuation', request.method)

    return functions.replace_punctuation(request)

@private.route('/status', methods=['GET', 'POST'])
def status():
    return common.status()

@private.route('/stopwords', methods=['GET', 'POST'])
@login_required
def stopwords():
    track_event('private', 'stopwords', request.method)

    return functions.remove_stop_words(request)

@private.route('/symbols', methods=['GET', 'POST'])
@login_required
def symbols():
    track_event('private', 'symbols', request.method)

    return functions.replace_symbols(request)

@private.route('/urls', methods=['GET', 'POST'])
@login_required
def urls():
    track_event('private', 'urls', request.method)

    return functions.replace_urls(request)

@private.route('/whitespaces', methods=['GET', 'POST'])
@login_required
def whitespaces():
    track_event('private', 'whitespaces', request.method)

    return functions.remove_extra_whitespaces(request)
