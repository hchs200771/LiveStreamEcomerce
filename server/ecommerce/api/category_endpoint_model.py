from flask_restplus import fields
from flask_restplus import reqparse
from ecommerce.api import abstract_model
from ecommerce.api.api_proxy import api


category_filter = abstract_model.page_filter.copy()

category_query = api.inherit('category_query', abstract_model.resource_common)

category_id = api.inherit('category_id', abstract_model.id)

category_create = api.model('category_create', {
    'name': fields.String(required=True, description='category name')
})
