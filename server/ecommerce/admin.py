import logging
from ecommerce import util
from ecommerce.persistence import ec_model
from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView

log = logging.getLogger(__name__)


class AdminModel(ModelView):
    can_create = False


@util.log_scope(log)
def init(app):
    admin = Admin(app, name='Ecommerce', template_mode='bootstrap3')
    admin.add_view(AdminModel(ec_model.Category))
    admin.add_view(AdminModel(ec_model.Product))
    admin.add_view(AdminModel(ec_model.Order))
    admin.add_view(AdminModel(ec_model.Product_Category))
    admin.add_view(AdminModel(ec_model.Order_Product))
    log.info('inited.')
