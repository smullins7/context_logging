
import logging
import web

from acme.lib import index, tlss

logger = logging.getLogger(__name__)

tls = tlss.tls

class IndexController(object):

    def GET(self):
        params = web.input()
        customer_name = params.get('name', 'UNKNOWN')
        tls.customer_name = customer_name
        logger.info("Received request")
        return index.get_index(customer_name)

class FooController(object):

    def GET(self, customer_name):
        tls.customer_name = customer_name
        logger.info("Received request")
        return index.get_index(customer_name)

urls = (
    '/', 'IndexController',
    '/foo/(.*)', 'FooController',
)
