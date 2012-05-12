"""Index request handler supporting code."""

import logging
import random

logger = logging.getLogger(__name__)

def get_index(name):
    logger.info("Doing work")
    return generate_random_number()

def generate_random_number():
    num = random.randint(1, 100)
    logger.info("Generated random number %d" % num)
    return num
