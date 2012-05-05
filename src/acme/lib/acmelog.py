
import logging
import web

class ContextFilter(logging.Filter):
    def filter(self, record):
        record.client_ip = web.ctx.env['REMOTE_ADDR']
        return True
context_filter = ContextFilter()
