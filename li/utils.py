import urllib

# API location info
API_SERVER = 'http://services.phila.gov/'
API_BASE = 'PhillyApi/Data/v0.7/Service.svc/'

# Default parameters applied to queries
DEFAULT_PARAMS = {
    '$format': 'json'  # Changing this to XML will break things
}

"""Names of keys that contain URLs to more details for requests.
For example, a permit may have additional information available
with the following entities 'locations', 'buildingboardappeals',
'zoningboardappeals'. This is a list of all those entity names
"""
DOC_TYPES = [
    'locations',
    'buildingboardappeals',
    'zoningboardappeals',
    'lireviewboardappeals',
    'appealhearings',
    'cases',
    'permits',
    'licenses',
    'violationdetails'
]


def construct_url(doc_type, query_params, sql):
    """Build a URL to query the API
    """
    f_query_params = construct_params(query_params)

    if sql:
        f_query_params += '&$filter=' + urllib.quote_plus(sql)

    url = API_SERVER + API_BASE + doc_type + f_query_params

    return url


def construct_params(query_params):
    """
    :query_params: a dictionary with param_name:value
    """
    params = '?'

    modified_params = {}

    # We need to put a '$' in front of every parameter name
    for k, v in query_params.keys():
        modified_params['$' + k] = v

    modified_params = apply_default_params(modified_params)

    params += urllib.urlencode(modified_params, True)

    return params


def apply_default_params(query_params):
    """Apply the default parameters to the query_params
    specified by the user
    """
    for k, v in DEFAULT_PARAMS.items():
        if k not in query_params.keys():
            query_params[k] = v

    return query_params


def get_deferred_urls(results):
    """Returns a list of URLS for all
    the deferred entities for a particular entity

    :results: the result for a call to get_permit,
    get_case, etc
    """
    urls = {}

    for doc in DOC_TYPES:
        if doc in results.keys():
            urls[doc] = results[doc]['__deferred']['uri']

    return urls
