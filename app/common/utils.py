from distutils.util import strtobool
from flask import make_response, jsonify

def get_data(request, keys):
    values = []

    data = request.get_json() if request.method == 'POST' else None

    for key in keys:
        if data:
            values.append(data[key] if key in data else None)
        else:
            values.append(request.values.get(key))

    return values

def prepare_response(result, keys, values):
    data = dict()

    for i, key in enumerate(keys):
        if values[i]:
            data[key] = list(values[i]) if isinstance(values[i], set) else values[i]

    data['text'] = result

    return make_response(jsonify(data))

def to_boolean(value, none_value=False):
    if value is None:
        value = none_value
    elif not isinstance(value, bool):
        try:
            value = strtobool(value)
        except ValueError:
            value = none_value

    return value
