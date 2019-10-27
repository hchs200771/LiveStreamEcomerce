import logging
from peewee import DoesNotExist, IntegrityError
from ecommerce import util
from ecommerce.exception import *
from ecommerce.persistence.ec_model import database_proxy, Category

log = logging.getLogger(__name__)


@util.log_scope(log)
def create(name):
    try:
        category = Category.create(name=name, created_date=util.current_time())
    except IntegrityError:
        raise ResourceExistedError()

    return category


@util.log_scope(log)
def find(page_number=1, items_per_page=25):
    if items_per_page == -1:
        category = Category.select().order_by(Category.id)
    else:
        category = Category.select().order_by(Category.id).paginate(page_number, items_per_page)

    return list(category)


@util.log_scope(log)
def find_one(category_id):
    try:
        category = Category.get(Category.id == category_id)
    except DoesNotExist:
        raise ResourceNotFound()

    return category


@util.log_scope(log)
def remove(category_id):
    try:
        category = Category.get(Category.id == category_id)
    except DoesNotExist:
        raise ResourceNotFound()

    cnt = Category.delete().where(Category.id == category_id).execute()
    log.debug('{} id: {} was deleted, cnt: {}'.format(__name__, category_id, cnt))


@util.log_scope(log)
def count():
    return Category.select(Category.id).count()
