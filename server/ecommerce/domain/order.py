import logging
from peewee import DoesNotExist, IntegrityError
from ecommerce import util
from ecommerce.exception import *
from ecommerce.persistence.ec_model import database_proxy, Product, Order, Order_Product

log = logging.getLogger(__name__)


class PaymentType(util.BaseEnum):
    CREDITCARD = 'Credit Card'
    ATM = 'ATM'
    DELIVERY = 'Payment on Delivery'


class OrderStatus(util.BaseEnum):
    UNPAID = 'Unpaid'
    UNSHIPPED = 'Unshipped'
    SHIPPED = 'Shipped'
    COMPLETE = 'Complete'


@util.log_scope(log)
def create(cust_name, cust_phone, cust_email, cust_addr, payment_type, product_id_collection):
    if payment_type not in PaymentType.to_list():
        raise DataValidationError('payment type error')
    if not product_id_collection:
        raise BusinessRuleValidationError('no product entered')

    total = 0
    product_list = []
    for product_id in product_id_collection:
        try:
            product = Product.get(Product.id == product_id)
        except DoesNotExist:
            raise DataValidationError('product id: {}'.format(product_id))

        total += product.price
        product_list.append(product)

    with database_proxy.atomic():
        order = Order.create(
            cust_name=cust_name,
            cust_phone=cust_phone,
            cust_email=cust_email,
            cust_addr=cust_addr,
            payment_type=payment_type,
            total=total,
            status=OrderStatus.UNPAID.value,
            created_date=util.current_time()
        )

        for product in product_list:
            Order_Product.create(order=order, product=product)

    return order


@util.log_scope(log)
def find(page_number=1, items_per_page=25):
    if items_per_page == -1:
        o_query = Order.select().order_by(Order.id)
    else:
        o_query = Order.select().order_by(Order.id).paginate(page_number, items_per_page)

    result = []
    for order in o_query:
        op_query = Order_Product.select().join(Order).where(Order.id == order.id)

        product_collection = []
        for q in list(op_query):
            product_collection.append({'id': q.product.id, 'name': q.product.name})

        item = {}
        item['id'] = order.id
        item['cust_name'] = order.cust_name
        item['cust_phone'] = order.cust_phone
        item['cust_email'] = order.cust_email
        item['cust_addr'] = order.cust_addr
        item['payment_type'] = order.payment_type
        item['total'] = order.total
        item['status'] = order.status
        item['created_date'] = order.created_date
        item['product_collection'] = product_collection
        result.append(item)

    return result


@util.log_scope(log)
def find_one(order_id):
    try:
        order = Order.get(Order.id == order_id)
    except DoesNotExist:
        raise ResourceNotFound()

    op_query = Order_Product.select().join(Order).where(Order.id == order.id)

    product_collection = []
    for q in list(op_query):
        product_collection.append({'id': q.product.id, 'name': q.product.name})

    item = {}
    item['id'] = order.id
    item['cust_name'] = order.cust_name
    item['cust_phone'] = order.cust_phone
    item['cust_email'] = order.cust_email
    item['cust_addr'] = order.cust_addr
    item['payment_type'] = order.payment_type
    item['total'] = order.total
    item['status'] = order.status
    item['created_date'] = order.created_date
    item['product_collection'] = product_collection

    return item


@util.log_scope(log)
def do_update(order_id, cust_name='', cust_phone='', cust_email='', cust_addr='', payment_type='', status='', product_id_collection=[]):
    try:
        order = Order.get(Order.id == order_id)
    except DoesNotExist:
        raise ResourceNotFound('order id: {}'.format(order_id))

    if (order.status == OrderStatus.SHIPPED.value) and (status == OrderStatus.COMPLETE.value):
        with database_proxy.atomic():
            order.status = status
            order.modified_date = util.current_time()
            order.save()

    if (order.status == OrderStatus.SHIPPED.value) or (order.status == OrderStatus.COMPLETE.value):
        raise BusinessRuleValidationError('order status is {}'.format(order.status))

    with database_proxy.atomic():
        if cust_name:
            order.cust_name = cust_name
        if cust_phone:
            order.cust_phone = cust_phone
        if cust_email:
            order.cust_email = cust_email
        if cust_addr:
            order.cust_addr = cust_addr
        if payment_type:
            if payment_type not in PaymentType.to_list():
                raise DataValidationError('payment type error')
            order.payment_type = payment_type
        if status:
            if status not in OrderStatus.to_list():
                raise DataValidationError('order status error')
            order.status = status
        if product_id_collection:
            Order_Product.delete().where(Order_Product.order == order.id).execute()

            for product_id in product_id_collection:
                try:
                    product = Product.get(Product.id == product_id)
                except DoesNotExist:
                    raise DataValidationError('product id: {}'.format(product_id))

                Order_Product.create(order=order, product=product)

        order.modified_date = util.current_time()
        order.save()
        log.debug('order saved: {}'.format(order))


@util.log_scope(log)
def remove(order_id):
    try:
        order = Order.get(Order.id == order_id)
    except DoesNotExist:
        raise ResourceNotFound()

    cnt = Order.delete().where(Order.id == order_id).execute()
    log.debug('{} id: {} was deleted, cnt: {}'.format(__name__, order_id, cnt))


@util.log_scope(log)
def count():
    return Order.select(Order.id).count()
