import logging
import time
from ecommerce import util
from ecommerce import admin
from ecommerce import app_config
from ecommerce.api import api_proxy
from ecommerce.persistence import ec_model
from flask import Flask, Blueprint, request, g

log = logging.getLogger(__name__)
flask_app = Flask(__name__)


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


@util.log_scope(log)
def init(config_obj):
    ec_model.init()

    flask_app.config.from_object(config_obj)
    if app_config.CONFIG.DEBUG:
        admin.init(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
    api_proxy.init(blueprint)
    flask_app.register_blueprint(blueprint)

    return flask_app
