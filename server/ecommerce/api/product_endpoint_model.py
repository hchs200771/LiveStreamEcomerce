from flask_restplus import fields
from flask_restplus import reqparse
from ecommerce.api import abstract_model
from ecommerce.api.api_proxy import api


product_filter = abstract_model.page_filter.copy()

product_query = api.inherit('product_query', abstract_model.product_with_all)

product_id = api.inherit('product_id', abstract_model.id)

product_create = api.model('product_create', {
    'name': fields.String(required=True, description='product name', example='BMW'),
    'brief': fields.String(description='product brief', example='a car'),
    'description': fields.String(description='product description', example='This is a car.'),
    'image': fields.String(required=True, description='product image url', example='https://image_url.jpg'),
    'category_id_collection': fields.List(fields.Integer(description='category id', example=1)),
    'original_price': fields.Integer(required=True, description='product original price', example=999),
    'special_price': fields.Integer(description='product special price', example=999)
})

product_reapply = api.model('product_reapply', {
    'name': fields.String(description='product name', example='BMW'),
    'brief': fields.String(description='product brief', example='a car'),
    'description': fields.String(description='product description', example='This is a car.'),
    'image': fields.String(description='product image url', example='https://image_url.jpg'),
    'category_id_collection': fields.List(fields.Integer(description='category id', example=1)),
    'original_price': fields.Integer(description='product original price', example=999),
    'special_price': fields.Integer(description='product special price', example=999)
})
