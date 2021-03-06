context_logging
===============

This project is a demonstration of using the Python logging framework to inject request context specific information into every log message, without passing that information into every log message function call.

example
-------
If your log format looked like this:

`FORMAT = "%(asctime)s|%(levelname)s|%(REMOTE_ADDR)s|%(CUSTOMER_NAME)s|%(message)s"`

The logging framework would not know what to do with `REMOTE_ADDR` and `CUSTOMER_NAME`.

Use the following filter in your logging config to inject these values into the log message:

    import logging
    from logmdc import filter
    filter = ContextFilter(keys=['REMOTE_ADDR', 'CUSTOMER_NAME'])
    logger = logging.getLogger()
    logger.addFilter(filter)

Now all you have to do is have code to set those values within a running process:

    from logmdc.storage import mapped_context
    mapped_context.put('CUSTOMER_NAME', 'foobar')
    mapped_context.put('REMOTE_ADDR', '127.0.0.1')

Of course, this isn't all that useful by itself. If you're using this within a web application/service, you can automatically pull information from HTTP headers in this web.py example:
    
    from logmdc.webheaders import HeaderRequestFilter
    header_filter = HeaderRequestFilter([
        "REMOTE_ADDR",
        "CUSTOMER_NAME",
    ])
    
    urls = ('/', 'IndexController')
    app = web.application(urls, globals())
    app.add_processor(web.loadhook(header_filter))
    app.run()

With this, any request to this web.py app will look for the headers `REMOTE_ADDR` and `CUSTOMER_NAME` and set their values in local storage for the logging filter to inject those values in the log message.

**Note** that customer HTTP client request headers get prefixed with `HTTP_` in web.py, as such the `HeaderRequestFilter` by default will strip that prefix out to prevent a mismatch between the value set by the client and header name used by the logging filter.

details
-------
The core logic involves usage of the following:
 * logging.filters
 * logging.config.dictConfig

This project contains a dummy application to showcase the usage of the context logging. The code for logging is under _src/logmdc_.
