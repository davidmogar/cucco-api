from distutils.util import strtobool
from flask import make_response, jsonify

def get_data(request, keys):
    """Return a list of data from the request.

    Returns a list of key:value pairs from the data of a request
    if the keys are defined.

    Attributes:
        request: Current request.
        keys: Keys to search for.

    Returns:
        A list of key:value pairs.
    """
    values = []

    data = request.get_json() if request.method == 'POST' else None

    for key in keys:
        if data:
            values.append(data[key] if key in data else None)
        else:
            values.append(request.values.get(key))

    return values

def prepare_response(result, keys, values):
    """Prepare the response for a request.

    Attributes:
        result: Result of the normalization.
        keys: Options used.
        values: Values for the options.

    Returns:
        A valid answer.
    """
    data = dict()

    for i, key in enumerate(keys):
        if values[i]:
            data[key] = list(values[i]) if isinstance(values[i], set) else values[i]

    data['text'] = result

    return make_response(jsonify(data))

def to_boolean(value, none_value=False):
    """Converts a value to boolean.

    Attributes:
        value: Value to convert.

    Returns:
        A boolean representing the value.
    """
    if value is None:
        value = none_value
    elif not isinstance(value, bool):
        try:
            value = strtobool(value)
        except ValueError:
            value = none_value

    return value
