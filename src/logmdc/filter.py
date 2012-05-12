
import logging

from logmdc.storage import thread_local_storage

class ContextFilter(logging.Filter):
    """Inject values into logging message"""

    def __init__(self, keys=None, default='NOT_SET'):
        """
        keys is a list of attributes to retrieve from thread local storage
        default is the value the log message will contain for each key that isn't found
        """
        self.keys = keys or []
        self.default = default

    def filter(self, record):
        for k in self.keys:
            value = thread_local_storage.__dict__.get(k, self.default)
            setattr(record, k, value)

        return True
