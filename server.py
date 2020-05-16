import os
#import logging

#LOG = logging.getLogger(__name__)
#LOG.setLevel(logging.DEBUG)

#handler = logging.FileHandler(filename='access.log')
#formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
#handler.setFormatter(formatter)
#handler.setLevel(logging.INFO)

#class OnlyInfoFilter:
#    def filter(self, logRecord):
#        return logRecord.levelno == logging.INFO

#handler.addFilter(OnlyInfoFilter())
#LOG.addHandler(handler)

import sentry_sdk

from bottle import Bottle, run, route
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://467421eea82648cc87488801d83d5bb4@o390139.ingest.sentry.io/5231108",
    integrations=[BottleIntegration()]
)

@route('/')
def index():
    return 'hello'

@route('/success')
def success():
    #LOG.info('hello!!!!!!!!!!!!!!!!!!')
    return 'все ок'

@route('/fail')
def fail():
    #LOG.info('fail!!!!!!!!!!!!!!!!!!')
    raise RuntimeError('this is the error message')
    return
  
if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host='localhost', port=8080)