import functions_framework
import json


@functions_framework.http
def add(request):
    """HTTP Cloud Function for addition."""
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'X' in request_json and 'Y' in request_json:
        X = request_json['X']
        Y = request_json['Y']
        if Y == 0:
            return 'Error: Division by zero is not allowed.'
        result = X + Y
    elif request_args and 'X' in request_args and 'Y' in request_args:
        X = request_args['X']
        Y = request_args['Y']
        if Y == 0:
            return 'Error: Division by zero is not allowed.'
        result = X + Y
    else:
        return 'Error: Please provide both "X" and "Y" parameters.'

    return json.dumps({
        "X": X,
        "Y": Y,
        "Result": result
    })
