__author__ = "James Alexander Levy (jamesalexanderlevy@gmail.com)"

import os, logging
CURRENT_DJANGO_VERSION = '1.0'
import google.appengine.dist
google.appengine.dist.use_library('django', CURRENT_DJANGO_VERSION)


from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.api import users
from django.utils import simplejson
		
import methods 

APP_TITLE = 'tweetbits'


			
class Index(webapp.RequestHandler):
    """
    Landing Page
    """
    def get(self):
			# set context
			context = {
			'title': APP_TITLE,
		  }
			# calculate the template path
			path = os.path.join(os.path.dirname(__file__), 'templates',
			    'index.html')
			# render the template with the provided context
			self.response.out.write(template.render(path, context))


class AjaxHandler(webapp.RequestHandler):
    def get(self):
      # calculate the template path
      path = os.path.join(os.path.dirname(__file__), 'templates',
          'ajax.html')
      context = {
        'codeid': '8074857350961',
        'handle': self.request.get('handle'),
        'twitter_stream': methods.twitter_stream(self.request.get('handle'))
      }
      # render the template with the provided context
      self.response.out.write(template.render(path, context))






# wire up the views
application = webapp.WSGIApplication([
    ('/', Index),
    ('/ajax', AjaxHandler),
], debug=True)

def main():
    "Run the application"
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
