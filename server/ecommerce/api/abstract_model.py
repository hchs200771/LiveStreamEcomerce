from flask_restplus import fields
from flask_restplus import reqparse
from ecommerce.api.api_proxy import api


page_filter = reqparse.RequestParser()
page_filter.add_argument('page_number', type=int, default=1, help='頁碼')
page_filter.add_argument('items_per_page', type=int, default=25, help='每頁顯示筆數, -1 means fetch all records.')

id = api.model('id', {
    'id': fields.Integer(required=False, description='abstract resource id'),
})

resource_common = api.model('resource_common', {
    'id': fields.Integer(required=True, description='resource id'),
    'name': fields.String(required=True, description='resource name'),
})
