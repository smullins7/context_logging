context_logging
===============

This project is a demonstration of using the Python logging framework to inject request context specific information into every log message, without passing that information into every log message function call.

The core logic involves usage of the following:
 * logging.filters
 * logging.config.dictConfig
 * threading.local

This project contains a dummy application to showcase the usage of the context logging. Once I have abstracted the context into a reusable form, the project will be divided into the logging context library, and the dummy application.

I am using this project as a case study for design best practices; the code is purposefully not designed for reuse, and will go through several iterations of improvements for the puporses of demonstrating design choices and tradeoffs.

Lastly, this is the *TODO* list for this project:
 * unit testing
 * abstract the request context, allowing ContextFilter to be extended
 * with an abstract context, what to do about the message format if anything?
 * abstract the request context gathering, apply to multiple controllers
