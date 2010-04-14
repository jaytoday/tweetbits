
API_LIST = 			    [

			    {
            'name': 'user',
            'description': '',
            'methods': [
              {
               'name': 'user.info',
               'description': 'Get information about a user',
               'query': 'username=billy',
              },
                            {
               'name': 'user.bits',
               'description': 'Get the bits attached by a user',
               'query': 'username=billy&skip=0&limit=20',
               'collection': 'bits'
              }
            ]
			    },

          {
            'name': 'code',
            'description': '',
            'methods': [
              {
               'name': 'code.get',
               'description': 'Get media and information associated with a code',
                'collection': 'media',
              'query': 'codeid=1'
              },
              {
               'name': 'code.popular',
               'description': 'Get a list of codes sorted by popularity',
               'collection': 'codes',
               'query': 'skip=0&limit=20',
             }
            ]
			    }
			    ]
