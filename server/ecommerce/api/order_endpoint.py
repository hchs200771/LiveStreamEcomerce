import logging
from flask import request
from flask_restplus import Resource
from ecommerce.api import order_endpoint_model as model
from ecommerce.api.api_proxy import api
from ecommerce.domain import order as OrderDO

log = logging.getLogger(__name__)
namespace = api.namespace('orders', description='Order management.')


@namespace.route('')
class Collection(Resource):

    @api.response(204, 'Success')
    def head(self):
        '''
        Get the number of orders.
        '''
        return None, 204, {'x-result-count': OrderDO.count()}

    @api.expect(model.order_filter, validate=True)
    @api.marshal_list_with(model.order_query)
    def get(self):
        '''
        Get orders collection.
        '''
        args = model.order_filter.parse_args(request)
        return OrderDO.find(**args)

    @api.expect(model.order_create, validate=True)
    @api.marshal_with(model.order_id, code=201)
    @api.response(201, 'Success')
    @api.response(403, 'DataValidationError, BusinessRuleValidationError')
    def post(self):
        '''
        Create a new order.

        - payment_type:
            - Credit Card
            - ATM
            - Payment on Delivery
        '''
        data = request.json
        order = OrderDO.create(**data)
        return {'id': order.id}, 201


@namespace.route('/<int:id>')
class Item(Resource):

    @api.marshal_with(model.order_query)
    @api.response(404, 'ResourceNotFound')
    def get(self, id):
        '''
        Get a order metadata.
        '''
        return OrderDO.find_one(id)

    @api.expect(model.order_reapply, validate=True)
    @api.response(204, 'Success')
    @api.response(403, 'DataValidationError, BusinessRuleValidationError')
    @api.response(404, 'ResourceNotFound')
    def put(self, id):
        '''
        Reapply order.
        '''
        data = request.json
        data['order_id'] = id
        OrderDO.do_update(**data)
        return None, 204

    @api.response(204, 'Success')
    @api.response(404, 'ResourceNotFound')
    def delete(self, id):
        '''
        Delete a order.
        '''
        OrderDO.remove(id)
        return None, 204
