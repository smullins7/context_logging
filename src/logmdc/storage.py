"""Thread local storage singleton"""

import threading

class MappedContext(object):

    def __init__(self):
        self._map = threading.local()

    def get(self, x, default=None):
        if self._map.__dict__.has_key(x):
            return self._map.__dict__.get(x)
        return default

    def put(self, x, value):
        setattr(self._map, x, value)

    def remove(self, x):
        self._map.__dict__.pop(x)

mapped_context = MappedContext()
