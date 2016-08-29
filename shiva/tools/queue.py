from flask import g
import beanstalkc
from shiva.common import settings


def _get_client():
    if not hasattr(g, 'beanstalk'):
        g.beanstalk = beanstalkc.Connection(host=settings.QUEUE_HOST, port=settings.QUEUE_PORT)
    return g.beanstalk


def put(data):
    client = _get_client()
    job_id = client.put(data)
    return job_id
