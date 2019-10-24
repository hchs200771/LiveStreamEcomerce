import os
import logging
import flask_restplus
import importlib
from ecommerce import util
from ecommerce import app_config
from ecommerce.exception import *

log = logging.getLogger(__name__)
api = flask_restplus.Api(version='1.0', title='LiveStreamEcommerce API', description='LiveStreamEcommerce API Document <style>.models {display: none !important}</style>')


@api.errorhandler
def default_error_handler(e):
    log.exception(e)
    message = 'An unhandled exception occurred.'
    return {'message': message}, 500


def _error_handler(e, code):
    msg = '{}: [{}]'.format(e.__class__.__name__, e)
    log.exception(e)
    return {'message': msg}, code


@api.errorhandler(DataValidationError)
def database_constraint_error_handler(e):
    return _error_handler(e, 403)


@api.errorhandler(BusinessRuleValidationError)
def database_constraint_error_handler(e):
    return _error_handler(e, 403)


@api.errorhandler(ResourceNotFound)
def resource_not_found_error_handler(e):
    return _error_handler(e, 404)


@api.errorhandler(ResourceExistedError)
def database_key_duplicated_error_handler(e):
    return _error_handler(e, 409)


@util.log_scope(log)
def init(app):
    if not app_config.CONFIG.DEBUG:
        api._doc = False

    api.init_app(app)

    import ecommerce
    for model_name in [os.path.splitext(f)[0] for f in os.listdir(list(ecommerce.api.__path__)[0])]:
        if model_name.endswith('_endpoint'):
            m = importlib.import_module('ecommerce.api.' + model_name)
            log.debug('endpoint: {} added.'.format(m.__name__))

    log.info('inited.')
