#!/usr/bin/env python

import logging
from logging import config
import web

FORMAT = "%(asctime)s,%(msecs)d|%(levelname)s|%(REMOTE_ADDR)s|%(CUSTOMER_NAME)s|%(name)s|%(funcName)s|%(message)s"
acme_logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'context_format': {
            'format': FORMAT,
        },
    },
    'filters': {
        'context_filter': {
            '()': 'logmdc.filter.ContextFilter',
            'keys': ['REMOTE_ADDR', 'CUSTOMER_NAME'],
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

if __name__ == "__main__":
    from acme.app.webserver import IndexController, FooController, urls, header_filter
    app = web.application(urls, globals())
    app.add_processor(web.loadhook(header_filter))
    app.run()
