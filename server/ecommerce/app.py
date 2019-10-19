import logging
from ecommerce import util
from ecommerce.api import api_proxy
from flask import Flask, Blueprint, request, g

log = logging.getLogger(__name__)
flask_app = Flask(__name__)


@util.log_scope(log)
def init(config_obj):
    flask_app.config.from_object(config_obj)

    blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
    api_proxy.init(blueprint)
    flask_app.register_blueprint(blueprint)

    return flask_app
