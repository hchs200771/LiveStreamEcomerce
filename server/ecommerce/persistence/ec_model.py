import logging
import peewee
from playhouse.postgres_ext import *
from ecommerce import util
from ecommerce.persistence import model_common

__all__ = ['database_proxy', 'DB_NAME', 'Category', 'Product', 'Product_Category',
           'Order', 'Order_Product', 'open_connection', 'close_connection', 'init']

log = logging.getLogger(__name__)
database_proxy = Proxy()
DB_NAME = 'ec'


class BaseModel(peewee.Model):
    class Meta:
        database = database_proxy
        only_save_dirty = True


class Category(BaseModel):
    id = AutoField()
    name = CharField(unique=True, index=True)
    created_date = DateTimeField(index=True, formats=['%Y-%m-%d %H:%M:%S'])

    def __str__(self):
        return '<{}: {}>'.format(self.id, self.name)


class Product(BaseModel):
    id = AutoField()
    name = CharField(index=True)
    brief = CharField(null=True)
    description = CharField(null=True)
    image = CharField()
    price = IntegerField(index=True)
    created_date = DateTimeField(index=True, formats=['%Y-%m-%d %H:%M:%S'])
    modified_date = DateTimeField(null=True, index=True, formats=['%Y-%m-%d %H:%M:%S'])

    def __str__(self):
        return '<{}: {}>'.format(self.id, self.name)


class Product_Category(BaseModel):
    product = ForeignKeyField(Product, on_delete='CASCADE')
    category = ForeignKeyField(Category, on_delete='CASCADE')

    def __str__(self):
        return '<product:{} category:{}>'.format(self.product_id, self.category_id)

    class Meta:
        indexes = (
            (('product', 'category'), True),
        )


class Order(BaseModel):
    id = AutoField()
    cust_name = CharField()
    cust_phone = CharField()
    cust_addr = CharField()
    cust_email = CharField()
    payment_type = CharField(index=True)
    total = IntegerField(index=True)
    status = CharField(index=True, constraints=[Check('status IN (\'Unpaid\', \'Unshipped\', \'Shipped\', \'Complete\')')])
    created_date = DateTimeField(index=True, formats=['%Y-%m-%d %H:%M:%S'])
    modified_date = DateTimeField(null=True, index=True, formats=['%Y-%m-%d %H:%M:%S'])

    def __str__(self):
        return '<{}: {}>'.format(self.id, self.status)


class Order_Product(BaseModel):
    order = ForeignKeyField(Order, on_delete='CASCADE')
    product = ForeignKeyField(Product, on_delete='CASCADE')
    quantity = IntegerField()

    def __str__(self):
        return '<order:{} product:{} quantity:{}>'.format(self.order_id, self.product_id, self.quantity)

    class Meta:
        indexes = (
            (('order', 'product'), True),
        )


def open_connection():
    database_proxy.connect()


def close_connection():
    database_proxy.close()


@util.log_scope(log)
def init(createdb=False):
    if (not model_common.is_database_exist(DB_NAME)) or createdb:
        model_common.create_model(__name__, DB_NAME)
    else:
        model_common.load_model(__name__, DB_NAME)

    log.info('{} inited.'.format(__name__))
