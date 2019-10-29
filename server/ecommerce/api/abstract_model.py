from flask_restplus import fields
from flask_restplus import reqparse
from ecommerce.api.api_proxy import api


page_filter = reqparse.RequestParser()
page_filter.add_argument('page_number', type=int, default=1, help='頁碼')
page_filter.add_argument('items_per_page', type=int, default=25, help='每頁顯示筆數, -1 means fetch all records.')

id = api.model('id', {
    'id': fields.Integer(required=False, description='abstract resource id'),
})

id_collection = api.model('id_collection', {
    'id_collection': fields.List(fields.Integer, required=True, description='abstract resource id'),
})

resource_common = api.model('resource_common', {
    'id': fields.Integer(required=True, description='resource id'),
    'name': fields.String(required=True, description='resource name'),
})

product_with_all = api.model('product_with_all', {
    'id': fields.Integer(required=True, description='product id', example=1),
    'name': fields.String(required=True, description='product name', example='BMW'),
    'brief': fields.String(description='product brief', example='a car'),
    'description': fields.String(description='product description', example='This is a car.'),
    'image': fields.String(required=True, description='product image url', example='https://image_url.jpg'),
    'price': fields.Integer(required=True, description='product price', example=999),
    'category_collection': fields.List(fields.Nested(resource_common, allow_null=True))
})
