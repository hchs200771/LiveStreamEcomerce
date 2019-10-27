from flask_restplus import fields
from flask_restplus import reqparse
from ecommerce.api import abstract_model
from ecommerce.api.api_proxy import api
from ecommerce.domain import order as OrderDO


order_filter = abstract_model.page_filter.copy()

order_query = api.model('order_query', {
    'id': fields.Integer(required=True, description='order id', example=1),
    'cust_name': fields.String(required=True, description='customer name', example='Jeffrey'),
    'cust_phone': fields.String(required=True, description='customer phone', example='0987654321'),
    'cust_email': fields.String(required=True, description='customer email', example='example@gmail.com'),
    'cust_addr': fields.String(required=True, description='customer address', example='Taipei ...'),
    'payment_type': fields.String(required=True, enum=OrderDO.PaymentType.to_list(), description='付款方式'),
    'total': fields.Integer(required=True, description='total price', example=999),
    'status': fields.String(required=True, enum=OrderDO.OrderStatus.to_list(), description='訂單狀態'),
    'created_date': fields.DateTime(required=True, description='order time'),
    'product_collection': fields.List(fields.Nested(abstract_model.resource_common))
})

order_id = api.inherit('order_id', abstract_model.id)

order_create = api.model('order_create', {
    'cust_name': fields.String(required=True, description='customer name', example='Jeffrey'),
    'cust_phone': fields.String(required=True, description='customer phone', example='0987654321'),
    'cust_email': fields.String(required=True, description='customer email', example='example@gmail.com'),
    'cust_addr': fields.String(required=True, description='customer address', example='Taipei ...'),
    'payment_type': fields.String(required=True, enum=OrderDO.PaymentType.to_list(), description='付款方式'),
    'product_id_collection': fields.List(fields.Integer(required=True, description='product id'))
})

order_reapply = api.model('order_reapply', {
    'cust_name': fields.String(description='customer name', example='Jeffrey'),
    'cust_phone': fields.String(description='customer phone', example='0987654321'),
    'cust_email': fields.String(description='customer email', example='example@gmail.com'),
    'cust_addr': fields.String(description='customer address', example='Taipei ...'),
    'payment_type': fields.String(enum=OrderDO.PaymentType.to_list(), description='付款方式'),
    'status': fields.String(enum=OrderDO.OrderStatus.to_list(), description='訂單狀態'),
    'product_id_collection': fields.List(fields.Integer(description='product id'))
})
