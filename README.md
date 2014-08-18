ckanext-cacheapi
================

CKAN extension: Clear NGINX caches.

setup
=====

NGINX
-----

Add proxy cache bypass cookie to your Nginx config file

proxy_cache_bypass $http_x_example;

http://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_cache_bypass

SETTINGS
--------

Set http_x_cookie_name to the cookie name used above.
 
ckanext.cacheapi.http_x_cookie_name = example

CKAN
----

You can either clear a URL, or group of URLS. 

To create a group of URLs, implement the ICache interface in your plugin

p.implements(ICache, inherit=True)

Which returns a dictionary of group names and list of URLS

# ICache
def get_caches(self, context, cache_dict):

    cache_dict['example_group'] = [
        'url1',
        'url2',
        ...
    ]
    
    return cache_dict
    
Commands
--------

You can then clear the cache with:

paster cache clear example_group -c path/to/config

Or for just a URL:

paster cache clear url -c path/to/config