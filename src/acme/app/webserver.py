
import logging
import web

from acme.lib import acmelog, index



FORMAT = "%(asctime)s,%(msecs)d|%(levelname)s|%(client_ip)s|%(name)s|%(funcName)s|%(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
logger = logging.getLogger(__name__)
logger.addFilter(acmelog.context_filter)

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
