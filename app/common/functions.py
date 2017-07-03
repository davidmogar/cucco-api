import json

from flask import abort
from cucco import Cucco

from app.common.utils import get_data, prepare_response, to_boolean

cucco = Cucco()

def _call(function, keys, values):
    """Invoke a funcion and prepare its response.

    This function invokes the function received as arguments with
    the given values and prepare a valid answer or abort the request
    if an error is found.

    Attributes:
        function: Function to invoke.
        keys: Keys to use on the response.
        values: Arguments to send to the function.

    Returns:
        A valid answer.
    """
    try:
      result = getattr(cucco, function)(*values)

      return prepare_response(result, keys, values)
    except Exception as e:
        abort(500, str(e))

def normalize(request):
    """Function to process execute normalize function."""

    keys = ['text', 'normalizations']
    values = get_data(request, keys)

    if not values[0]:
        abort(400, 'missing text parameter')

    if not values[1]:
        values[1] = cucco._config.normalizations

    return _call('normalize', keys, values)

def remove_accent_marks(request):
    """Function to process execute remove_accent_makrs function."""
    keys = ['text']
    values = get_data(request, keys)

    if not values[0]:
        abort(400, 'missing text parameter')

    return _call('remove_accent_marks', keys, values)

def remove_extra_white_spaces(request):
    """Function to process execute remove_extra_white_spaces function."""
    keys = ['text']
    values = get_data(request, keys)

    if not values[0]:
        abort(400, 'missing text parameter')

    return _call('remove_extra_white_spaces', keys, values)

def remove_stop_words(request):
    """Function to process execute remove_stop_words function."""
    keys = ['text', 'ignore_case', 'language']
    values = get_data(request, keys)

    if not values[0]:
        abort(400, 'missing text parameter')

    values[1] = to_boolean(values[1], True)

    return _call('remove_stop_words', keys, values)

def replace_characters(request):
    """Function to process execute replace_characters function."""
    keys = ['text', 'characters', 'replacement']
    values = get_data(request, keys)

    if not values[0]:
        abort(400, 'missing text parameter')

    if not values[2]:
        values[2] = ''

    return _call('replace_characters', keys, values)

def replace_emails(request):
    """Function to process execute replace_emails function."""
    keys = ['text', 'replacement']
    values = get_data(request, keys)

    if not values[0]:
        abort(400, 'missing text parameter')

    if not values[1]:
        values[1] = ''

    return _call('replace_emails', keys, values)

def replace_emojis(request):
    """Function to process execute replace_emojis function."""
    keys = ['text', 'replacement']
    values = get_data(request, keys)

    if not values[0]:
        abort(400, 'missing text parameter')

    if not values[1]:
        values[1] = ''

    return _call('replace_emojis', keys, values)

def replace_hyphens(request):
    """Function to process execute replace_hyphens function."""
    keys = ['text', 'replacement']
    values = get_data(request, keys)

    if not values[0]:
        abort(400, 'missing text parameter')

    if not values[1]:
        values[1] = ''

    return _call('replace_hyphens', keys, values)

def replace_punctuation(request):
    """Function to process execute replace_punctuation function."""
    keys = ['text', 'excluded', 'replacement']
    values = get_data(request, keys)

    if not values[0]:
        abort(400, 'missing text parameter')

    if values[1]:
        values[1] = set(values[1])

    if not values[2]:
        values[2] = ''

    return _call('replace_punctuation', keys, values)

def replace_symbols(request):
    """Function to process execute replace_symbols function."""
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

    return _call('replace_symbols', keys, values)

def replace_urls(request):
    """Function to process execute replace_urls function."""
    keys = ['text', 'replacement']
    values = get_data(request, keys)

    if not values[0]:
        abort(400, 'missing text parameter')

    if not values[1]:
        values[1] = ''

    return _call('replace_urls', keys, values)
