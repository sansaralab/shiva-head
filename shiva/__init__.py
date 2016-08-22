from flask import Flask, g
from shiva.tools.request import error
app = Flask(__name__, template_folder='head/dst')


@app.errorhandler(404)
def not_found(err):
    return error({'message': 'Not found'}, 404)


@app.errorhandler(405)
def not_allowed(err):
    return error({'message': 'Method not allowed'}, 405)


import shiva.head.views
