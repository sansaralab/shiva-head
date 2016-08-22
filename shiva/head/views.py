from flask import render_template, Response, request
from shiva import app


@app.route('/')
def index():
    return 'Hello Shiva'


@app.route('/tracker.js', methods=['GET'])
def serve_track_js():
    return Response(
        render_template('tracker.min.js', server=request.host_url),
        mimetype='application/javascript')
