import logging
from flask import request
from flask_restplus import Resource
from ecommerce.api import product_endpoint_model as model
from ecommerce.api.api_proxy import api
from ecommerce.domain import product as ProductDO

log = logging.getLogger(__name__)
namespace = api.namespace('products', description='Product management.')


@namespace.route('')
class Collection(Resource):

    @api.response(204, 'Success')
    def head(self):
        '''
        Get the number of products.
        '''
        return None, 204, {'x-result-count': ProductDO.count()}

    @api.expect(model.product_filter, validate=True)
    @api.marshal_list_with(model.product_query)
    def get(self):
        '''
        Get products collection.
        '''
        args = model.product_filter.parse_args(request)
        return ProductDO.find(**args)

    @api.expect(model.product_create, validate=True)
    @api.marshal_with(model.product_id, code=201)
    @api.response(201, 'Success')
    @api.response(403, 'DataValidationError')
    def post(self):
        '''
        Create a new product.
        '''
        data = request.json
        product = ProductDO.create(**data)
        return {'id': product.id}, 201


@namespace.route('/<int:id>')
class Item(Resource):

    @api.marshal_with(model.product_query)
    @api.response(404, 'ResourceNotFound')
    def get(self, id):
        '''
        Get a product metadata.
        '''
        return ProductDO.find_one(id)

    @api.expect(model.product_reapply, validate=True)
    @api.response(204, 'Success')
    @api.response(403, 'DataValidationError')
    @api.response(404, 'ResourceNotFound')
    def put(self, id):
        '''
        Reapply produce.
        '''
        data = request.json
        data['product_id'] = id
        ProductDO.do_update(**data)
        return None, 204

    @api.response(204, 'Success')
    @api.response(404, 'ResourceNotFound')
    def delete(self, id):
        '''
        Delete a product.
        '''
        ProductDO.remove(id)
        return None, 204
