
import logging
import web

from acme.lib import index

class ContextFilter(logging.Filter):
    def filter(self, record):
        record.client_ip = web.ctx.env['REMOTE_ADDR']
        return True

context_filter = ContextFilter()

FORMAT = "%(asctime)s,%(msecs)d|%(levelname)s|%(client_ip)s|%(name)s|%(funcName)s|%(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
logger = logging.getLogger(__name__)
logger.addFilter(context_filter)

class IndexController(object):

    def GET(self):
        logger.info("Received request")
        params = web.input()
        return index.get_index(params.get('name', 'UNKNOWN'))

urls = (
    '/', 'IndexController',
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
