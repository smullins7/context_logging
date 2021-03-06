
from logmdc.storage import mapped_context
from functools import wraps
import web


class HeaderRequestFilter(object):
    """Stores specified request headers for later use."""

    def __init__(self, header_keys, strip_http=True):
        """
        header_keys is a list of header names that will be stored
        strip_http will remove the prefix 'HTTP_' from the stored header
        """
        self.header_keys = header_keys
        self.strip_http = strip_http

    def __call__(self):
        for k in self._get_header_keys(web.ctx.env.keys()):
            mapped_context.put(self._strip_http(k), web.ctx.env[k])

    def _get_header_keys(self, keys):
        for k in keys:
            if k in self.header_keys:
                yield k
            elif self._strip_http(k) in self.header_keys:
                yield k

    def _strip_http(self, k):
        if not self.strip_http or not k.startswith('HTTP_'):
            return k
        return k.split('_', 1)[1]


class HeaderRequestFilterDecorator(HeaderRequestFilter):

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            self.store()
            return func(*args, **kwargs)
        return wrapper

