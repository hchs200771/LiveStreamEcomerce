import logging
from ecommerce import util

log = logging.getLogger(__name__)


class PaymentType(util.BaseEnum):
    CREDITCARD = 'Credit Card'
    ATM = 'ATM'
    DELIVERY = 'Payment on Delivery'


class OrderStatus(util.BaseEnum):
    UNPAID = 'Unpaid'
    UNSHIPPED = 'Unshipped'
    SHIPPED = 'Shipped'
    COMPLETE = 'Complete'
