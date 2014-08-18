import logging
import requests
import urlparse
import ckan.plugins as p
import ckan.lib.navl.dictization_functions
from ckanext.cacheapi.logic.schema import cache_clear_schema
from ckanext.cacheapi.interfaces import ICache
from ckanext.cacheapi.exceptions import CacheUrlException
import ckan.logic as logic
import ckan.model as model
from ckan.common import c
from pylons import config

NotFound = logic.NotFound
get_action = logic.get_action
_get_or_bust = logic.get_or_bust
_validate = ckan.lib.navl.dictization_functions.validate

log = logging.getLogger(__name__)

def cache_clear(context, data_dict):

    """
    Retrieve an individual record
    @param context:
    @param data_dict:
    @return:
    """

    # Validate the data
    context = {'model': model, 'session': model.Session, 'user': c.user or c.author}
    schema = context.get('schema', cache_clear_schema())
    data_dict, errors = _validate(data_dict, schema, context)

    if errors:
        raise p.toolkit.ValidationError(errors)

    cache = data_dict.get('cache')

    cache_dict = {}
    for plugin in p.PluginImplementations(ICache):
        cache_dict = plugin.get_caches(context, cache_dict)

    try:
        # Is this a cache group (relating to a group of URLs defined in ICache)
        cache_urls = cache_dict[cache]
    except KeyError:
        # Otherwise, we're going to assume it's a URL
        cache_urls = [cache]

    for cache_url in cache_urls:
        log.info('Clearing cache for path %s', cache_url)
        proxy_cache_bypass(cache_url)


def proxy_cache_bypass(url):
    """
    Function to call http://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_cache_bypass for a URL
    @param url: url to clear
    @return: status
    """
    url = urlparse.urljoin(config.get('ckan.site_url'), url)
    http_x_cookie = 'X-%s' % config.get('ckanext.cacheapi.http_x_cookie_name')
    r = requests.head(url, headers={http_x_cookie: 1})

    if r.headers['x-cache-status'] == 'BYPASS':
        log.info('Successfully cleared cache for path %s', url)
    else:
        raise CacheUrlException('Cache for URL %s could not be cleared' % url)