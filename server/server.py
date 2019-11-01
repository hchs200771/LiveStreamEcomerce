import time
import os
import urllib.parse
import subprocess
import logging
import logging.config
from ecommerce import util
from ecommerce import admin
from ecommerce import app_config
from ecommerce import logging_config
from ecommerce.api import api_proxy
from ecommerce.persistence import ec_model
from shutil import which
from flask import Flask, Blueprint, request, g
from flask_cors import CORS

log = logging.getLogger(__name__)
flask_app = Flask(__name__)

if os.environ.get('PRODUCT_ENVIRONMENT') == 'production':
    app_config.CONFIG = app_config.ProductionConfig
else:
    app_config.CONFIG = app_config.DevelopmentConfig

if os.environ.get('ON_HEROKU'):
    urllib.parse.uses_netloc.append('postgres')
    url = urllib.parse.urlparse(os.environ['DATABASE_URL'])
    app_config.CONFIG.POSTGRES_DBNAME = url.path[1:]
    app_config.CONFIG.POSTGRES_HOST = url.hostname
    app_config.CONFIG.POSTGRES_PORT = url.port
    app_config.CONFIG.POSTGRES_USER = url.username
    app_config.CONFIG.POSTGRES_PASSWORD = url.password
else:
    if which('docker') is None:
        raise Exception('docker not installed.')
    if which('docker-compose') is None:
        raise Exception('docker-compose not installed.')
    subprocess.run('docker-compose -f docker-compose.yml up -d', shell=True)

ec_model.init()
flask_app.config.from_object(app_config.CONFIG)
if app_config.CONFIG.DEBUG:
    admin.init(flask_app)

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api_proxy.init(blueprint)
flask_app.register_blueprint(blueprint)
CORS(flask_app)


@flask_app.before_request
def before_request():
    log.info('request: {}'.format(' '.join([request.remote_addr, request.method, request.url])))
    if flask_app.config['DEBUG']:
        g.request_start_time = time.time()
        g.request_time = lambda: '%.5fs' % (time.time() - g.request_start_time)
        log.debug('request header: {}'.format(', '.join([': '.join(x) for x in request.headers])))
        log.debug('request data: {}'.format(request.get_data(as_text=True)))

    ec_model.open_connection()


@flask_app.after_request
def after_request(response):
    ec_model.close_connection()

    if flask_app.config['DEBUG']:
        response.headers.add('x-time-elpased', g.request_time())

    return response


if __name__ == '__main__':
    try:
        if os.environ.get('ON_HEROKU'):
            flask_app.run()
        else:
            flask_app.run(host=app_config.CONFIG.SERVER_HOST, port=app_config.CONFIG.SERVER_PORT)
    except Exception:
        import traceback
        traceback.print_exc()
