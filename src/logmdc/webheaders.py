
from logmdc.storage import thread_local_storage
from functools import wraps
import web

class StoreHeaders(object):
    """Stores specified request headers for later use."""

    def __init__(self, header_keys, strip_http=True):
        """
        header_keys is a list of header names that will be stored
        strip_http will remove the prefix 'HTTP_' from the stored header
        """
        self.header_keys = header_keys
        self.strip_http = strip_http

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for k in self._get_header_keys(web.ctx.env.keys()):
                self._store(k, web.ctx.env[k])
            return func(*args, **kwargs)
        return wrapper

    def _store(self, k, v):
        setattr(thread_local_storage, self._strip_http(k), v)

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
