import ckan.plugins.interfaces as interfaces

class ICache(interfaces.Interface):

    def get_caches(self, context, cache_dict):
        '''

        List of caches available to clear
        These are keyed by the name of the cache
        With a list of URLs related to the cache

        {
            'example': [
                '/url/1',
                'url/2'
            ]
        }

        '''

        return cache_dict
