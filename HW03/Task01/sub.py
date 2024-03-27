import functions_framework


@functions_framework.http
def subtract(request):
    """HTTP Cloud Function for subtraction."""
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'num1' in request_json and 'num2' in request_json:
        num1 = request_json['num1']
        num2 = request_json['num2']
        result = num1 - num2
    elif request_args and 'num1' in request_args and 'num2' in request_args:
        num1 = request_args['num1']
        num2 = request_args['num2']
        result = num1 - num2
    else:
        return 'Error: Please provide both "num1" and "num2" parameters.'

    return str(result)
