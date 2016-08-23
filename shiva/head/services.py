import uuid
from urllib.parse import urlparse
from time import time
from shiva.domain.types import UserVisit, UserData


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


def send_visit_to_queue(visit: UserVisit):
    pass


def send_action_to_queue(action: UserData):
    pass
