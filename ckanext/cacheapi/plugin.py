import os
import ckan.plugins as p
import ckanext.cacheapi.logic.action as action


Invalid = p.toolkit.Invalid

class CacheAPIPlugin(p.SingletonPlugin):
    """
    Cache API plugin - for modifying NGINX caches
    """
    p.implements(p.IActions, inherit=True)

    # IActions
    def get_actions(self):

        return {
            'cache_clear':  action.cache_clear
        }