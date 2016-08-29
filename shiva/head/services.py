import uuid
from urllib.parse import urlparse
from time import time
from flask.json import dumps
from shiva.domain.types import UserVisit, UserData
from shiva.tools.queue import put


def new_user_id():
    return str(uuid.uuid4())


def get_or_create_user_id(request):
    user_id = request.cookies.get('userid', None)
    if user_id is None:
        user_id = new_user_id()
    return user_id


def update_userid_cookie(request, response):
    user_id = get_or_create_user_id(request)
    host = request.host_url
    parsed_uri = urlparse(host)
    domain = '{uri.netloc}'.format(uri=parsed_uri)
    response.set_cookie(
        key='userid', value=user_id, httponly=True,
        expires=time() + 315360000, domain=domain)
    return user_id


def add_allow_all_origins_header(request, response):
    response.headers['Access-Control-Allow-Origin'] = request.referrer.strip('/')
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Max-Age'] = 1728000
    response.headers['Access-Control-Allow-Headers'] = \
        'DNT,X-CustomHeader,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type, ' \
        'Set-Cookie'


def send_visit_to_queue(visit: UserVisit):
    data = dumps(visit._asdict())
    return put(data)


def send_action_to_queue(action: UserData):
    data = dumps(action._asdict())
    return put(data)
