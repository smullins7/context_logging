
import logging
import web

from acme.lib.tlss import tls

class ContextFilter(logging.Filter):
    def filter(self, record):
        record.client_ip = web.ctx.env['REMOTE_ADDR']
        record.customer_name = tls.__dict__.get('customer_name', 'NOT_SET')
        return True

def ContextFilterFactory():
    return ContextFilter()
