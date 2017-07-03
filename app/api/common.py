from flask import Blueprint, make_response, jsonify, request

from app.common import functions
from app.common.analytics import track_event

common = Blueprint('common', __name__, url_prefix='/')

def status():
    track_event('common', 'status', request.method)

    return make_response(jsonify({ 'status': 'ok' }))
