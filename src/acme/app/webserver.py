
import web

class IndexController(object):

    def GET(self):
        return "Hello, world!"

urls = (
    '/', 'IndexController',
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
