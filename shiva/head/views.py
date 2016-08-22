from urllib.parse import urlparse
from time import time
from flask import render_template, make_response, request
from shiva import app
from .services import new_user_id


@app.route('/')
def index():
    return 'Hello Shiva'


@app.route('/tracker.js', methods=['GET'])
def serve_track_js():
    user_id = request.cookies.get('userid', None)
    resp = make_response(render_template('tracker.min.js', server=request.host_url))
    resp.headers['Content-Type'] = 'application/javascript; charset=utf-8'
    if user_id is None:
        host = request.host_url
        parsed_uri = urlparse(host)
        domain = '{uri.netloc}'.format(uri=parsed_uri)
        resp.set_cookie(
            key='userid', value=new_user_id(), httponly=True,
            expires=time() + 315360000, domain=domain)
    return resp
