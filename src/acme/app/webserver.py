
import logging
import web

from acme.lib import index
from logmdc.webheaders import HeaderRequestFilter

logger = logging.getLogger(__name__)

header_filter = HeaderRequestFilter([
    "REMOTE_ADDR",
    "CUSTOMER_NAME",
])

class IndexController(object):

    def GET(self):
        params = web.input()
        customer_name = params.get('name', 'UNKNOWN')
        logger.info("Received request")
        return index.get_index(customer_name)

class FooController(object):

    def GET(self, customer_name):
        return index.get_index(customer_name)

urls = (
    '/', 'IndexController',
    '/foo/(.*)', 'FooController',
)
