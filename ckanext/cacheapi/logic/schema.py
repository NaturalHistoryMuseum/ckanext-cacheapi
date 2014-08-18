import ckan.plugins as p

get_validator = p.toolkit.get_validator

# Core validators and converters
not_missing = get_validator('not_missing')

def cache_clear_schema():

    schema = {
        'cache': [not_missing, unicode],
    }

    return schema
