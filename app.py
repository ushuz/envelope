# coding: utf-8

import os

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.log import access_log
from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class NovenHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("noven.html")


handlers = [
    (r"/", MainHandler),
    (r"/noven", NovenHandler),
]

settings = {
    "debug": os.getenv('ENV') == 'dev',
    "gzip": True,
    "static_url_prefix": os.getenv('ENVELOPE_STATIC_URL_PREFIX', '/static/'),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
}

# Set access log level to WARNING
access_log.setLevel(30)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    application = tornado.web.Application(handlers, **settings)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
