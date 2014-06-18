"""
WSGI config for ditch project.

This is the websocket config

"""
import os
import gevent.monkey
import redis.connection
redis.connection.socket = gevent.socket
os.environ.update(DJANGO_SETTINGS_MODULE='ditch.settings.dev')
from ws4redis.uwsgi_runserver import uWSGIWebsocketServer
application = uWSGIWebsocketServer()
