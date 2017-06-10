import json

from flask import abort
from cucco import Cucco

from app.common.utils import get_data, prepare_response, to_boolean

cucco = Cucco()

def remove_accent_marks(request):
    keys = ['text']
    values = get_data(request, keys)

    if not values[0]:
        abort(400, 'missing text parameter')

    result = cucco.remove_accent_marks(values[0])

    return prepare_response(result, keys, values)

def remove_extra_whitespaces(request):
    keys = ['text']
    values = get_data(request, keys)

    if not values[0]:
        abort(400, 'missing text parameter')

    result = cucco.remove_extra_whitespaces(values[0])

    return prepare_response(result, keys, values)

def remove_stop_words(request):
    keys = ['text', 'ignore_case', 'language']
    values = get_data(request, keys)

    if not values[0]:
        abort(400, 'missing text parameter')

    result  =cucco.remove_stop_words(values[0],
                                   to_boolean(values[1], True),
                                   values[2])

    return prepare_response(result, keys, values)

def replace_characters(request):
    keys = ['text', 'characters', 'replacement']
    values = get_data(request, keys)

    if not values[0]:
        abort(400, 'missing text parameter')

    if not values[2]:
        values[2] = ''

    result = cucco.replace_characters(values[0],
                                      values[1],
                                      values[2])

    return prepare_response(result, keys, values)

def replace_emails(request):
    keys = ['text', 'replacement']
    values = get_data(request, keys)

    if not values[0]:
        abort(400, 'missing text parameter')

    if not values[1]:
        values[1] = ''

    result = cucco.replace_emails(values[0], values[1])

    return prepare_response(result, keys, values)

def replace_emojis(request):
    keys = ['text', 'replacement']
    values = get_data(request, keys)

    if not values[0]:
        abort(400, 'missing text parameter')

    if not values[1]:
        values[1] = ''

    result = cucco.replace_emojis(values[0], values[1])

    return prepare_response(result, keys, values)

def replace_hyphens(request):
    keys = ['text', 'replacement']
    values = get_data(request, keys)

    if not values[0]:
        abort(400, 'missing text parameter')

    if not values[1]:
        values[1] = ''

    result = cucco.replace_hyphens(values[0], values[1])

    return prepare_response(result, keys, values)

def replace_punctuation(request):
    keys = ['text', 'excluded', 'replacement']
    values = get_data(request, keys)

    if not values[0]:
        abort(400, 'missing text parameter')

    if values[1]:
        values[1] = set(values[1])

    if not values[2]:
        values[2] = ''

    result = cucco.replace_punctuation(values[0],
                                       values[1],
                                       values[2])

    return prepare_response(result, keys, values)

def replace_symbols(request):
    keys = ['text', 'form', 'excluded', 'replacement']
    values = get_data(request, keys)

    if not values[0]:
        abort(400, 'missing text parameter')

    if not values[1]:
        values[1] = 'NFKD'

    if values[2]:
        values[2] = set(values[2])

    if not values[3]:
        values[3] = ''

    result = cucco.replace_symbols(values[0],
                                   values[1],
                                   values[2],
                                   values[3])

    return prepare_response(result, keys, values)

def replace_urls(request):
    keys = ['text', 'replacement']
    values = get_data(request, keys)

    if not values[0]:
        abort(400, 'missing text parameter')

    if not values[1]:
        values[1] = ''

    result = cucco.replace_urls(values[0], values[1])

    return prepare_response(result, keys, values)
