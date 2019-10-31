import logging
from peewee import DoesNotExist, IntegrityError
from ecommerce import util
from ecommerce.exception import *
from ecommerce.persistence.ec_model import database_proxy, Category, Product, Product_Category

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


@util.log_scope(log)
def find_children(category_id, page_number=1, items_per_page=25):
    query = Category.select().where(Category.id == category_id)
    if query.count() == 0:
        raise ResourceNotFound()

    if items_per_page == -1:
        p_query = Product_Category.select().join(Category).where(Category.id == category_id).order_by(Product_Category.id)
    else:
        p_query = Product_Category.select().join(Category).where(Category.id == category_id).order_by(Product_Category.id).paginate(page_number, items_per_page)

    result = []
    for q in list(p_query):
        pc_query = Product_Category.select().join(Product).where(Product.id == q.product.id)

        category_collection = []
        for pc in list(pc_query):
            category_collection.append({'id': pc.category.id, 'name': pc.category.name})

        item = {}
        item['id'] = q.product.id
        item['name'] = q.product.name
        item['brief'] = q.product.brief
        item['description'] = q.product.description
        item['image'] = q.product.image
        item['original_price'] = q.product.original_price
        item['special_price'] = q.product.special_price
        item['category_collection'] = category_collection
        result.append(item)

    return result
