import logging
from flask import request
from flask_restplus import Resource
from ecommerce.api import order_endpoint_model as model
from ecommerce.api.api_proxy import api

log = logging.getLogger(__name__)
namespace = api.namespace('orders', description='Order management.')


@namespace.route('')
class Collection(Resource):

    @api.response(204, 'Success')
    def head(self):
        '''
        Get the number of orders.
        '''
        api.abort(501)

    @api.expect(model.order_filter, validate=True)
    @api.marshal_list_with(model.order_query)
    def get(self):
        '''
        Get orders collection.
        '''
        api.abort(501)

    @api.expect(model.order_create, validate=True)
    @api.marshal_with(model.order_id, code=201)
    @api.response(201, 'Success')
    @api.response(403, 'DataValidationError')
    def post(self):
        '''
        Create a new order.
        '''
        api.abort(501)


@namespace.route('/<int:id>')
class Item(Resource):

    @api.marshal_with(model.order_query)
    @api.response(404, 'ResourceNotFound')
    def get(self, id):
        '''
        Get a order metadata.
        '''
        api.abort(501)

    @api.expect(model.order_reapply, validate=True)
    @api.response(204, 'Success')
    @api.response(403, 'DataValidationError, BusinessRuleValidationError')
    @api.response(404, 'ResourceNotFound')
    def put(self, id):
        '''
        Reapply order.
        '''
        api.abort(501)

    @api.response(204, 'Success')
    @api.response(403, 'BusinessRuleValidationError')
    @api.response(404, 'ResourceNotFound')
    def delete(self, id):
        '''
        Delete a order.
        '''
        api.abort(501)
