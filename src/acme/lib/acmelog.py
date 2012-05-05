
import logging
import web

from acme.lib import tlss

class ContextFilter(logging.Filter):
    def filter(self, record):
        record.client_ip = web.ctx.env['REMOTE_ADDR']
        tls = tlss.tls
        record.customer_name = tls.__dict__.get('customer_name', 'NOT_SET')
        return True

context_filter = ContextFilter()
