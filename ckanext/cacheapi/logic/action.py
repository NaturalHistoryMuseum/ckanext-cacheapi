import logging

import ckan.plugins as p
import ckan.lib.navl.dictization_functions
from ckanext.cacheapi.logic.schema import cache_clear_schema
import ckan.logic as logic
import ckan.model as model
from ckan.common import c

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

    cache_id = data_dict.get('cache_id')

    # Clear the cache
    log.info('Clearing cache %s', cache_id)



