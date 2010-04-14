from memoize import memoize
from web_services import twitter,stickybits

@memoize(force_cache=True)
def twitter_streams():
  streams = []
  api = twitter.Api('yupgrade', 'trixie')
  for name in ['jamtoday','seth','billychasen']:
    streams.append({
      'name': name, 
      'items': api.GetUserTimeline(name, count=5) 
    })
  return streams

@memoize()
def stickybits_streams():
  return [
			  {
			   'name': 'Stream',
			   'items': [ "one", "two", "three" ]
			  },
			  {
			   'name': 'Stream',
			   'items':  [ "one", "two", "three" ]
			  }
			]
