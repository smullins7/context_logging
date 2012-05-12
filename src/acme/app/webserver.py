
import logging
import web

from acme.lib import index
from logmdc.webheaders import StoreHeaders

logger = logging.getLogger(__name__)

store_headers = StoreHeaders([
    "REMOTE_ADDR",
    "CUSTOMER_NAME",
])

class IndexController(object):

    @store_headers
    def GET(self):
        params = web.input()
        customer_name = params.get('name', 'UNKNOWN')
        logger.info("Received request")
        return index.get_index(customer_name)

class FooController(object):

    @store_headers
    def GET(self, customer_name):
        return index.get_index(customer_name)

urls = (
    '/', 'IndexController',
    '/foo/(.*)', 'FooController',
)
