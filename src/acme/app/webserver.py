
from functools import wraps
import logging
import web

from acme.lib import index, tlss

logger = logging.getLogger(__name__)

tls = tlss.tls

def set_client_headers_in_tls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for k, v in web.ctx.env.items():
            if k.startswith('HTTP_'):
                setattr(tls, k.split('_', 1)[1].lower(), v)

        return func(*args, **kwargs)
    return wrapper

class IndexController(object):

    @set_client_headers_in_tls
    def GET(self):
        params = web.input()
        customer_name = params.get('name', 'UNKNOWN')
        logger.info("Received request")
        return index.get_index(customer_name)

class FooController(object):

    @set_client_headers_in_tls
    def GET(self, customer_name):
        return index.get_index(customer_name)

urls = (
    '/', 'IndexController',
    '/foo/(.*)', 'FooController',
)
