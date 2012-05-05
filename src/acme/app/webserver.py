
import logging
import web

from acme.lib import acmelog, index, tlss

FORMAT = "%(asctime)s,%(msecs)d|%(levelname)s|%(client_ip)s|%(customer_name)s|%(name)s|%(funcName)s|%(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
logger = logging.getLogger(__name__)
logger.addFilter(acmelog.context_filter)

class IndexController(object):

    def GET(self):
        params = web.input()
        customer_name = params.get('name', 'UNKNOWN')
        tls = tlss.tls
        tls.customer_name = customer_name
        logger.info("Received request")
        return index.get_index(customer_name)

urls = (
    '/', 'IndexController',
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
