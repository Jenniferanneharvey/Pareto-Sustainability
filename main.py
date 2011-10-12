#!/usr/bin/env python

import tornado.ioloop
import tornado.web
import tornado.options
from tornado.options import options

import logging
import os.path

tornado.options.define('port', 8080, int)

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    self.render('index.html')

def main():
  settings = {
    'debug': True,
    'template_path':'templates',
    'static_path':'static',
  }

  # setup the application.
  application = tornado.web.Application([
    # authentications
    ('/', MainHandler),
    ], **settings)

  application.listen(options.port)
  logging.info('Starting server on port %d', options.port)
  tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
  main()
