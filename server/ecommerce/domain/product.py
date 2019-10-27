import logging
from peewee import DoesNotExist, IntegrityError
from ecommerce import util
from ecommerce.exception import *
from ecommerce.persistence.ec_model import database_proxy, Product, Category, Product_Category

log = logging.getLogger(__name__)


@util.log_scope(log)
def create(name, image, price, brief='', description='', category_id_collection=[]):
    with database_proxy.atomic():
        product = Product.create(
            name=name,
            image=image,
            price=price,
            brief=brief,
            description=description,
            created_date=util.current_time()
        )

        for category_id in category_id_collection:
            try:
                category = Category.get(Category.id == category_id)
            except DoesNotExist:
                raise DataValidationError('category id: {}'.format(category_id))

            Product_Category.create(product=product, category=category)

    return product


@util.log_scope(log)
def find(page_number=1, items_per_page=25):
    if items_per_page == -1:
        p_query = Product.select().order_by(Product.id)
    else:
        p_query = Product.select().order_by(Product.id).paginate(page_number, items_per_page)

    result = []
    for product in p_query:
        pc_query = Product_Category.select().join(Product).where(Product.id == product.id)

        category_collection = []
        for q in list(pc_query):
            category_collection.append({'id': q.category.id, 'name': q.category.name})

        item = {}
        item['id'] = product.id
        item['name'] = product.name
        item['brief'] = product.brief
        item['description'] = product.description
        item['image'] = product.image
        item['price'] = product.price
        item['category_collection'] = category_collection
        result.append(item)

    return result


@util.log_scope(log)
def find_one(product_id):
    try:
        product = Product.get(Product.id == product_id)
    except DoesNotExist:
        raise ResourceNotFound()

    pc_query = Product_Category.select().join(Product).where(Product.id == product.id)

    category_collection = []
    for q in list(pc_query):
        category_collection.append({'id': q.category.id, 'name': q.category.name})

    item = {}
    item['id'] = product.id
    item['name'] = product.name
    item['brief'] = product.brief
    item['description'] = product.description
    item['image'] = product.image
    item['price'] = product.price
    item['category_collection'] = category_collection

    return item


@util.log_scope(log)
def do_update(product_id, name='', image='', price=0, brief='', description='', category_id_collection=[]):
    try:
        product = Product.get(Product.id == product_id)
    except DoesNotExist:
        raise ResourceNotFound('product id: {}'.format(product_id))

    with database_proxy.atomic():
        if name:
            product.name = name
        if image:
            product.image = image
        if price:
            product.price = price
        if brief:
            product.brief = brief
        if description:
            product.description = description
        if category_id_collection:
            Product_Category.delete().where(Product_Category.product == product.id).execute()

            for category_id in category_id_collection:
                try:
                    category = Category.get(Category.id == category_id)
                except DoesNotExist:
                    raise DataValidationError('category id: {}'.format(category_id))

                Product_Category.create(product=product, category=category)

        product.modified_date = util.current_time()
        product.save()
        log.debug('product saved: {}'.format(product))


@util.log_scope(log)
def remove(product_id):
    try:
        product = Product.get(Product.id == product_id)
    except DoesNotExist:
        raise ResourceNotFound()

    cnt = Product.delete().where(Product.id == product_id).execute()
    log.debug('{} id: {} was deleted, cnt: {}'.format(__name__, product_id, cnt))


@util.log_scope(log)
def count():
    return Product.select(Product.id).count()
