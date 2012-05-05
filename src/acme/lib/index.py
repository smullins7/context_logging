"""Index request handler supporting code."""

import logging
import random
import web

class ContextFilter(logging.Filter):
    def filter(self, record):
        record.client_ip = web.ctx.env['REMOTE_ADDR']
        return True

context_filter = ContextFilter()

logger = logging.getLogger(__name__)
logger.addFilter(context_filter)

def get_index(name):
    logger.info("Doing work for %s" % name)
    return generate_random_number()

def generate_random_number():
    num = random.randint(1, 100)
    logger.info("Generated random number %d" % num)
    return num
