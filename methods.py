from memoize import memoize
from web_services import twitter,stickybits, ttp
import logging

TEST_URL = "http://dev.stickybits.com/api/1/"
API_KEY = "c1e1928908a544dbc15b5e0231887a58"


@memoize(5000, force_cache=True)
def twitter_stream(name):
  logging.info('spaget!')
  api = twitter.Api('yupgrade', 'trixie')
  #parser = ttp.Parser()
  return api.GetUserTimeline(name, count=15)
  


@memoize()
def stickybits_streams():
  sb = stickybits.Stickybits(base_url=TEST_URL,
  api_key=API_KEY)
  sb.basicAuth('jamtoday','test')
  
  return [
			  {
			   'name': 'Stream',
			   'items': []#sb.bit.stream()
			  },
			  {
			   'name': 'Stream',
			   'items':  [ "one", "two", "three" ]
			  }
			]
