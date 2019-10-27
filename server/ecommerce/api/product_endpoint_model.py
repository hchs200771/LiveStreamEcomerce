from flask_restplus import fields
from flask_restplus import reqparse
from ecommerce.api import abstract_model
from ecommerce.api.api_proxy import api


product_filter = abstract_model.page_filter.copy()

product_query = api.model('product_query', {
    'id': fields.Integer(required=True, description='product id', example=1),
    'name': fields.String(required=True, description='product name', example='BMW'),
    'brief': fields.String(description='product brief', example='a car'),
    'description': fields.String(description='product description', example='This is a car.'),
    'image': fields.String(required=True, description='product image url', example='https://image_url.jpg'),
    'price': fields.Integer(required=True, description='product price', example=999),
    'category_collection': fields.List(fields.Nested(abstract_model.resource_common, allow_null=True))
})

product_id = api.inherit('product_id', abstract_model.id)

product_create = api.model('product_create', {
    'name': fields.String(required=True, description='product name', example='BMW'),
    'brief': fields.String(description='product brief', example='a car'),
    'description': fields.String(description='product description', example='This is a car.'),
    'image': fields.String(required=True, description='product image url', example='https://image_url.jpg'),
    'category_id_collection': fields.List(fields.Integer(description='category id', example=1)),
    'price': fields.Integer(required=True, description='product price', example=999)
})

product_reapply = api.model('product_reapply', {
    'name': fields.String(description='product name', example='BMW'),
    'brief': fields.String(description='product brief', example='a car'),
    'description': fields.String(description='product description', example='This is a car.'),
    'image': fields.String(description='product image url', example='https://image_url.jpg'),
    'category_id_collection': fields.List(fields.Integer(description='category id', example=1)),
    'price': fields.Integer(description='product price', example=999)
})
