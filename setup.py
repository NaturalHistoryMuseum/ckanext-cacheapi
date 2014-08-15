from setuptools import setup, find_packages

version = '0.1'

setup(
	name='ckanext-cacheapi',
	version=version,
	description='CKAN Extension providing API for clearing NGINX caches',
	classifiers=[],
	keywords='',
	author='Ben Scott',
	author_email='ben@benscott.co.uk',
	url='',
	license='',
    packages=find_packages(exclude=['tests']),
    namespace_packages=['ckanext', 'ckanext.cacheapi'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[],
	entry_points=\
	"""

	    [ckan.plugins]
            cacheapi = ckanext.cacheapi.plugin:CacheAPIPlugin

	    [paste.paster_command]
            cache=ckanext.cacheapi.commands.cache:CacheCommand
	""",
)