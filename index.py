__author__ = "James Alexander Levy (jamesalexanderlevy@gmail.com)"

import os, logging
CURRENT_DJANGO_VERSION = '1.0'
import google.appengine.dist
try:
  google.appengine.dist.use_library('django', CURRENT_DJANGO_VERSION)
except google.appengine.dist._library.UnacceptableVersionError:
  logging.error('UNABLE TO LOAD DJANGO %s' % CURRENT_DJANGO_VERSION)
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.api import users

import app_settings, methods




class Index(webapp.RequestHandler):
    """
    Landing Page
    """
    def get(self):
			# set context
			context = {
			  'api_base': 'http://stickybits.com/api/',
			  'apis': methods.API_LIST
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




class MobileHomeView(webapp.RequestHandler):
    """
    Landing Page
    """
    def get(self):
			# set context
			import random
			NAMES = ['Bon Jovi', 'Axl Rose', 'David Lee Roth']
			GADGET_NAMES = NAMES[:]
			random.shuffle(GADGET_NAMES)			
			GADGET_CODES = ['Google Nexus One', 'Motorola Droid', 'Apple iPad']
			random.shuffle(GADGET_CODES)
			
			FILM_NAMES = NAMES[:]
			random.shuffle(FILM_NAMES)
			FILM_CODES = ['Clash of the Titans', 'The Runaways', 'Iron Man 2']
			random.shuffle(FILM_CODES)
			
			GOODGUIDE_NAMES = NAMES[:]
			random.shuffle(GOODGUIDE_NAMES)
			GOODGUIDE_CODES = ['Dr.Bronners Citrus Shampoo', "Burt's Bee's Lip Balm", 'Terressentials Fragrance']
			random.shuffle(GOODGUIDE_CODES)
			
			context = {
			'activity_streams': [
			{
			'name': 'Gadgets',
			'items': [ ("""

			<div style="clear:both;"><a href="/c/6928784167558/oXJqoGQnhVXpi7xbG9CE4m">%s %s %s</a></div>

			<a href="/c/6928784167558/oXJqoGQnhVXpi7xbG9CE4m"><img src="http://dummyimage.com/%dx%d/000/fff" style=" margin:3px; clear:both;"/></a>
			
			""" % (GADGET_NAMES.pop(),
			random.choice(('attached a bit to', 'scanned')),
			GADGET_CODES.pop(),
			random.choice(range(50,100)), 
			random.choice(range(50,100)))
			) for e in range(3) ]
			},
			{
			'name': 'Films',
			'items': [ ("""

			<div style="clear:both;"><a href="/c/6928784167558/oXJqoGQnhVXpi7xbG9CE4m">%s %s %s</a></div>

			<a href="/c/6928784167558/oXJqoGQnhVXpi7xbG9CE4m"><img src="http://dummyimage.com/%dx%d/000/fff" style=" margin:3px; clear:both;"/></a>
			
			""" % (FILM_NAMES.pop(),
			random.choice(('attached a bit to', 'scanned')),
			FILM_CODES.pop(),
			random.choice(range(50,100)), 
			random.choice(range(50,100)))
			) for e in range(3) ]
			},
			{
			'name': 'GoodGuide',
			'items': [ ("""

			<div style="clear:both;"><a href="/c/6928784167558/oXJqoGQnhVXpi7xbG9CE4m">%s %s %s</a></div>

			<a href="/c/6928784167558/oXJqoGQnhVXpi7xbG9CE4m"><img src="http://dummyimage.com/%dx%d/000/fff" style=" margin:3px; clear:both;"/></a>
			
			""" % (GOODGUIDE_NAMES.pop(),
			random.choice(('attached a bit to', 'scanned')),
			GOODGUIDE_CODES.pop(),
			random.choice(range(50,100)), 
			random.choice(range(50,100)))
			) for e in range(3) ]
			}
			]
			}

			# calculate the template path
			path = os.path.join(os.path.dirname(__file__), 'templates',
			    'mobile_home.html')
			# render the template with the provided context
			self.response.out.write(template.render(path, context))

class MobileCodeView(webapp.RequestHandler):
    """
    Mobile view of code pages
    """
    def get(self):
			# set context
			import random
			context = {
			  'api_base': 'http://stickybits.com/api/',
			  'apis': methods.API_LIST,
			  'code': {
			    'name': 'code name',
			    'images': [(random.choice(range(50,60)), random.choice(range(40,70)), random.choice(['Bon Jovi', 'Axl Rose', 'David Lee Roth']), i + 1) for i in range(15)],
			    'videos': [(random.choice(range(50,60)), random.choice(range(40,70)), random.choice(['Bon Jovi', 'Axl Rose', 'David Lee Roth']), i + 1) for i in range(4)],
			    'comments': [("Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor...", random.choice(['Bon Jovi', 'Axl Rose', 'David Lee Roth']), i + 1) for i in range(10)],
			    'scanned_by': [i for i in range(8)],
			   
			    }
			    }
			# calculate the template path
			path = os.path.join(os.path.dirname(__file__), 'templates',
			    'mobile_code.html')
			# render the template with the provided context
			self.response.out.write(template.render(path, context))
			


# wire up the views
application = webapp.WSGIApplication([
    ('/324101383720', Index),
    ('/ajax', AjaxHandler),
    ('/', MobileHomeView),
    ('/c/.*', MobileCodeView)

], debug=True)

def main():
    "Run the application"
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
