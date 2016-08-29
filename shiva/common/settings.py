import os


APP_HOST = os.environ.get('APP_HEAD_HOST', '127.0.0.1')
APP_PORT = os.environ.get('APP_HEAD_PORT', 3000)
APP_DEBUG = os.environ.get('APP_HEAD_DEBUG', True)

QUEUE_HOST = os.environ.get('APP_QUEUE_HOST', '127.0.0.1')
QUEUE_PORT = os.environ.get('APP_QUEUE_PORT', 11300)
