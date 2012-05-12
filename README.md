context_logging
===============

This project is a demonstration of using the Python logging framework to inject request context specific information into every log message, without passing that information into every log message function call.

example
-------
If you're log format looked like this:
`FORMAT = "%(asctime)s|%(levelname)s|%(REMOTE_ADDR)s|%(CUSTOMER_NAME)s|%(message)s"`

The logging framework would not know what to do with `REMOTE_ADDR` and `CUSTOMER_NAME`.

Use the following filter in your logging config to inject these values into the log message:
`logmdc.filter.ContextFilter(keys=['REMOTE_ADDR', 'CUSTOMER_NAME'])`

Now all you have to do is have code to set those values within a running process:

    from logmdc.storage import mapped_context
    mapped_context.put('CUSTOMER_NAME', 'foobar')
    mapped_context.put('REMOTE_ADDR', '127.0.0.1')

Of course, this isn't all that useful by itself. If you're using this within a web application/service, you can automatically pull information from HTTP headers in this web.py example:
    
    from logmdc.webheaders import StoreHeaders
    store_headers = StoreHeaders([
        "REMOTE_ADDR",
        "CUSTOMER_NAME",
    ])
    
    class IndexController(object):

        @store_headers
        def GET(self):
            return 'OK'

With this, any request to the IndexController with look for the headers `REMOTE_ADDR` and `CUSTOMER_NAME` and set them in local storage for the logging filter to inject them in the log message.

**Note** that customer HTTP client request headers get prefixed with `HTTP_` in web.py, as such the `StoreHeaders` decorator by default will strip that prefix out to prevent a mismatch between the value set by the client and header name used by the logging filter.

details
-------
The core logic involves usage of the following:
 * logging.filters
 * logging.config.dictConfig

This project contains a dummy application to showcase the usage of the context logging. The code for logging is under _src/logmdc_.

I am using this project as a case study for design best practices; the code is purposefully not designed for reuse, and will go through several iterations of improvements for the puporses of demonstrating design choices and tradeoffs.

*TODO* list for this project:
 * unit testing
