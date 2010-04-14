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
			'twitter_streams': methods.twitter_streams(),
			'stickybits_streams': methods.stickybits_streams(),
		  }
			# calculate the template path
			path = os.path.join(os.path.dirname(__file__), 'templates',
			    'index.html')
			# render the template with the provided context
			self.response.out.write(template.render(path, context))


class AjaxHandler(webapp.RequestHandler):
    def get(self):
      from google.appengine.api import urlfetch
      fetch_page = urlfetch.fetch(
      'http://dev.stickybits.com/api/' + self.request.get('request_path'),
      headers = {'User-Agent': "Mozilla/5.0"}, deadline=15)
      from django.utils import simplejson
      logging.info(fetch_page.headers)
      logging.info(fetch_page.content)
      status_code = str(fetch_page.status_code)
      if status_code == '200':
        status_code += ' OK'
      else: status_code += ' Error'
      status_code = 'HTTP/1.1 ' + status_code
      content = simplejson.loads(fetch_page.content)
      content = simplejson.dumps(content, indent=4)
      import re
      content = re.sub('"(.*)":', self.renderProperty, content)
      # also replace resource URLs
      context = {
        'headers': fetch_page.headers.items(),
        'status_code' : status_code,
        'content': content
          }
      # calculate the template path
      path = os.path.join(os.path.dirname(__file__), 'templates',
          'api_response.html')
      # render the template with the provided context
      self.response.out.write(template.render(path, context))
    
    def renderProperty(self, matchobj):
      return '<span class="property">' + matchobj.group(0)[:-1] + '</span>:'






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
