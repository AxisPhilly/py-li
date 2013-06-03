import urllib
import requests

from .exceptions import LIException
from .settings import *


def validate_doc_type(doc_type):
    try:
        DOC_TYPES.index(doc_type)
    except ValueError:
        raise LIException('The provided doc_type is invalid.')


def validate_doc_id(doc_id, doc_type):
    """Some of the document endpoints take the unique document id
    as a number and not a string. For the ones that take a string,
    we have to add a single quotes to the doc_id
    """

    # doc_types that don't want singled-quoted doc_id
    doc_types = [
        'locations',
        'buildingboardappeals',
        'appealhearings',
        'lireviewboardappeals',
        'violationdetails',
        'zoningboardappeals'
    ]

    if doc_type not in doc_types:
        try:
            doc_id = "\'" + doc_id + "\'"
        except:
            raise TypeError('The first parameter must be the document id and a string')

    return doc_id


def invoke_api(url):
    """Make a call to the API with the provided URL
    and return the results
    """
    r = requests.get(url)
    results = r.json()

    if 'error' in results.keys():
        return {'error': results}
    elif 'results' in results['d'].keys():
        return results['d']['results']
    else:
        return results['d']


def get_related(results):
    """Make calls to the 'deferred'/related document
    types contained in the provided results object
    """
    deferred_urls = get_deferred_urls(results)

    for entity, url in deferred_urls.items():
        r = requests.get(url + '?$format=json')
        related = r.json()
        results[entity] = related['d']

    return results


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
