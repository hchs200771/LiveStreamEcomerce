import logging
from flask import request
from flask_restplus import Resource
from ecommerce.api import product_endpoint_model as model
from ecommerce.api.api_proxy import api

log = logging.getLogger(__name__)
namespace = api.namespace('products', description='Product management.')


@namespace.route('')
class Collection(Resource):

    @api.response(204, 'Success')
    def head(self):
        '''
        Get the number of products.
        '''
        api.abort(501)

    @api.expect(model.product_filter, validate=True)
    @api.marshal_list_with(model.product_query)
    def get(self):
        '''
        Get products collection.
        '''
        api.abort(501)

    @api.expect(model.product_create, validate=True)
    @api.marshal_with(model.product_id, code=201)
    @api.response(201, 'Success')
    @api.response(409, 'ResourceExistedError')
    def post(self):
        '''
        Create a new product.
        '''
        api.abort(501)


@namespace.route('/<int:id>')
class Item(Resource):

    @api.marshal_with(model.product_query)
    @api.response(404, 'ResourceNotFound')
    def get(self, id):
        '''
        Get a product metadata.
        '''
        api.abort(501)

    @api.expect(model.product_reapply, validate=True)
    @api.response(204, 'Success')
    @api.response(403, 'DataValidationError')
    @api.response(404, 'ResourceNotFound')
    def put(self, id):
        '''
        Reapply produce.
        '''
        api.abort(501)

    @api.response(204, 'Success')
    @api.response(403, 'BusinessRuleValidationError')
    @api.response(404, 'ResourceNotFound')
    def delete(self, id):
        '''
        Delete a product.
        '''
        api.abort(501)
