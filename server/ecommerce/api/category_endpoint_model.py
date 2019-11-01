from flask_restplus import fields
from flask_restplus import reqparse
from ecommerce.api import abstract_model
from ecommerce.api.api_proxy import api


category_filter = abstract_model.page_filter.copy()
category_filter.add_argument('with_product', type=int, default=0, help='with_product=1 會列出商品')

category_item_filter = reqparse.RequestParser()
category_item_filter.add_argument('with_product', type=int, default=0, help='with_product=1 會列出商品')

category_query = api.model('category_query', {
    'id': fields.Integer(required=True, description='resource id'),
    'name': fields.String(required=True, description='resource name'),
    'products': fields.List(fields.Nested(abstract_model.product_with_all))
})

category_id = api.inherit('category_id', abstract_model.id)

category_create = api.model('category_create', {
    'name': fields.String(required=True, description='category name')
})

category_product_query = api.inherit('category_product_query', abstract_model.product_with_all)
