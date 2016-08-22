from flask import jsonify


def success(data=dict(), code=200):
    ok = {
        'ok': True
    }

    response = jsonify(dict(data, **ok))
    response.status_code = code

    return response


def error(data=dict(), code=404):
    err = {
        'ok': False
    }

    response = jsonify(dict(data, **err))
    response.status_code = code

    return response
