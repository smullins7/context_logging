"""Index request handler supporting code."""

import logging
import random
import web

from acme.lib import acmelog

logger = logging.getLogger(__name__)
logger.addFilter(acmelog.context_filter)

def get_index(name):
    logger.info("Doing work", extra={'customer_name': name})
    return generate_random_number()

def generate_random_number():
    num = random.randint(1, 100)
    logger.info("Generated random number %d" % num)
    return num
