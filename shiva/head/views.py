from flask import render_template, make_response, request, jsonify
from shiva import app
from shiva.domain.types import UserVisit, UserData
from .services import update_userid_cookie, get_or_create_user_id, send_visit_to_queue, send_action_to_queue, \
    add_allow_all_origins_header


@app.route('/')
def index():
    return 'Hello Shiva'


@app.route('/shiva.js', methods=['GET'])
def serve_track_js():
    resp = make_response(render_template('tracker.min.js', server=request.host_url))
    add_allow_all_origins_header(request, resp)
    update_userid_cookie(request, resp)
    resp.headers['Content-Type'] = 'application/javascript; charset=utf-8'
    return resp


@app.route('/tracker/visit', methods=['GET'])
def track_visit():
    user_id = get_or_create_user_id(request)
    data = UserVisit(
        ip=request.remote_addr,
        page=request.args.get('page', None),
        user_agent=str(request.user_agent),
        user_id=user_id
    )
    send_visit_to_queue(data)
    resp = make_response(jsonify(dict(ok=True, userid=user_id)))
    add_allow_all_origins_header(request, resp)
    update_userid_cookie(request, resp)
    return resp


@app.route('/tracker/action', methods=['POST'])
def track_action():
    user_id = get_or_create_user_id(request)
    data = UserData(
        user_id=user_id,
        action_type=request.form.get('type', None),
        action_name=request.form.get('name', None),
        action_value=request.form.get('value', None)
    )
    send_action_to_queue(data)
    resp = make_response(jsonify(dict(ok=True)))
    add_allow_all_origins_header(request, resp)
    update_userid_cookie(request, resp)
    return resp
