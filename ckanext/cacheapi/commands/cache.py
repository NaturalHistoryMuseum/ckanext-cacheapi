
from ckan.plugins import toolkit
from ckan.lib.cli import CkanCommand

class CacheCommand(CkanCommand):
    """
    Create / Add / Delete type from the dataset type vocabulary

    Commands:
        paster cache clear proxy_cache_path -c <config>
        paster cache clear cache_id -c /etc/ckan/default/development.ini

    Where:
        <config> = path to your ckan config file

    The commands should be run from the ckanext-cacheapi directory.

    """
    summary = __doc__.strip().split('\n')[0]
    usage = '\n' + __doc__
    context = None

    def command(self):

        if not self.args or self.args[0] in ['--help', '-h', 'help']:
            print self.__doc__
            return

        cmd = self.args[0].replace('-', '_')

        if cmd.startswith('_'):
            print 'Cannot call private command %s' % cmd
            return

        self._load_config()

        # Set up context
        user = toolkit.get_action('get_site_user')({'ignore_auth': True}, {})
        self.context = {'user': user['name']}

        # Call the command method
        getattr(self, cmd)()


    def clear(self):

        try:
            data = {'cache': self.args[1]}
        except IndexError:
            print 'ERROR: cache ID not specified'
            print self.usage
        else:
            toolkit.get_action('cache_clear')(self.context, data)