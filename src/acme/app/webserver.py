
import logging
import web

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class IndexController(object):

    def GET(self):
        logger.info("Received request from %s" % web.ctx.env['REMOTE_ADDR'])
        return "Hello, world!"

urls = (
    '/', 'IndexController',
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
