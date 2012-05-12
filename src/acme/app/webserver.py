
import logging
import web

from acme.lib import index, headers

logger = logging.getLogger(__name__)


class IndexController(object):

    @headers.store_client_headers
    def GET(self):
        params = web.input()
        customer_name = params.get('name', 'UNKNOWN')
        logger.info("Received request")
        return index.get_index(customer_name)

class FooController(object):

    @headers.store_client_headers
    def GET(self, customer_name):
        return index.get_index(customer_name)

urls = (
    '/', 'IndexController',
    '/foo/(.*)', 'FooController',
)
