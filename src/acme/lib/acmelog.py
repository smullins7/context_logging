
import logging
import web

class ContextFilter(logging.Filter):
    def filter(self, record):
        record.client_ip = web.ctx.env['REMOTE_ADDR']
        if not record.__dict__.has_key('customer_name'):
            record.customer_name = 'NOT_SET'
        return True
context_filter = ContextFilter()
