
from acme.lib.tlss import tls
from functools import wraps
import web

def get_client_headers_from(headers):
    #client headers start with HTTP_
    for k, v in headers:
        if k.startswith('HTTP_'):
            yield k.split('_', 1)[1], v

def store_client_headers(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for k,v in get_client_headers_from(web.ctx.env.items()):
            setattr(tls, k.lower(), v)

        return func(*args, **kwargs)
    return wrapper
