import logging
from flask import request
from flask_restplus import Resource
from ecommerce.api import category_endpoint_model as model
from ecommerce.api.api_proxy import api
from ecommerce.domain import category as CategoryDO

log = logging.getLogger(__name__)
namespace = api.namespace('categories', description='Product category.')


@namespace.route('')
class Collection(Resource):

    @api.response(204, 'Success')
    def head(self):
        '''
        Get the number of categories.
        '''
        return None, 204, {'x-result-count': CategoryDO.count()}

    @api.expect(model.category_filter, validate=True)
    @api.marshal_list_with(model.category_query, skip_none=True)
    def get(self):
        '''
        Get categories collection.
        '''
        args = model.category_filter.parse_args(request)
        return CategoryDO.find(**args)

    @api.expect(model.category_create, validate=True)
    @api.marshal_with(model.category_id, code=201)
    @api.response(201, 'Success')
    @api.response(409, 'ResourceExistedError')
    def post(self):
        '''
        Create a new category.
        '''
        data = request.json
        category = CategoryDO.create(**data)
        return {'id': category.id}, 201


@namespace.route('/<int:id>')
class Item(Resource):

    @api.expect(model.category_item_filter, validate=True)
    @api.marshal_with(model.category_query, skip_none=True)
    @api.response(404, 'ResourceNotFound')
    def get(self, id):
        '''
        Get a category.
        '''
        args = model.category_item_filter.parse_args(request)
        return CategoryDO.find_one(id, **args)

    @api.response(204, 'Success')
    @api.response(404, 'ResourceNotFound')
    def delete(self, id):
        '''
        Delete a category.
        '''
        CategoryDO.remove(id)
        return None, 204


@namespace.route('/<int:id>/products')
class Product(Resource):

    @api.expect(model.category_filter, validate=True)
    @api.marshal_list_with(model.category_product_query)
    @api.response(404, 'ResourceNotFound')
    def get(self, id):
        '''
        Get all products in this category.
        '''
        args = model.category_filter.parse_args(request)
        return CategoryDO.find_children(id, **args)
