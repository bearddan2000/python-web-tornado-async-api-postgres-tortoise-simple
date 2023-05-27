from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.web import Application

from handlers import *

define('host', default='0.0.0.0', help='Docker specific address')
define('port', default=8000, help='port to listen on')

def main():
    """Construct and serve the tornado application."""
    app = Application([
        ('/', SmokeTestHandler)
        , ('/dog', GetHandler)
    ])

    http_server = HTTPServer(app)
    http_server.listen(options.port, options.host)
    print(f'Listening on http://{options.host}:{options.port}')
    
    IOLoop.current().start()

if __name__ == '__main__':
    main()
