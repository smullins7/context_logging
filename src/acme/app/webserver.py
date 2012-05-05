
import logging
from logging import config
import web

from acme.lib import index, tlss

FORMAT = "%(asctime)s,%(msecs)d|%(levelname)s|%(client_ip)s|%(customer_name)s|%(name)s|%(funcName)s|%(message)s"
acme_logging_config = {
    'version': 1,
    'formatters': {
        'context_format': {
            'format': FORMAT,
        },
    },
    'filters': {
        'context_filter': {
            '()': 'acme.lib.acmelog.ContextFilterFactory',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'context_format',
            'level': logging.INFO,
            'filters': ['context_filter'],
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': logging.INFO,
            'propagate': True,
        },
    },
}

config.dictConfig(acme_logging_config)
logger = logging.getLogger(__name__)

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
