import urllib
import requests

from .exceptions import DocTypeException, DocIDException
from .settings import *


def validate_doc_type(doc_type):
    """Make sure the provided doc_type is
    supported
    """
    try:
        DOC_TYPES.index(doc_type)
    except ValueError:
        raise DocTypeException


def validate_doc_id(doc_id, doc_type):
    """Some of the document endpoints take the unique document id
    as a number and not a string. For the ones that take a string,
    we have to add a single quotes to the doc_id
    """
    if doc_type not in NUMBER_DOC_TYPE:
        try:
            doc_id = "\'" + doc_id + "\'"
        except TypeError:
            raise DocIDException

    return doc_id


def construct_url(doc_type, **kwargs):
    """Build a URL to query the API
    """
    # Construct a dict of just the ODATA query parameters
    query_params = {}

    for arg in kwargs:
        if arg in QUERY_PARAMS:
            query_params[arg] = kwargs[arg]

    # Count isn't a real query param, but better than inlinecount=allpages
    # We let user say count=True, then add inlinecount=allpages for them
    if 'count' in kwargs and kwargs['count'] is True:
        query_params['inlinecount'] = 'allpages'

    f_query_params = construct_params(query_params)

    url = API_SERVER + API_BASE + doc_type + f_query_params

    return url


def construct_params(query_params):
    """
    :query_params: a dictionary with param_name:value
    """
    params = '?'

    full_params = apply_default_params(query_params)

    # We need to put a '$' in front of every parameter name
    modified_params = {}

    for k, v in full_params.items():
        modified_params['$' + k] = v

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


def invoke_api(url):
    """Make a call to the API with the provided URL
    and return the results
    """
    r = requests.get(url)
    results = r.json()

    response = process_results(results)

    return response


def process_results(results):
    """Construct the request response into a
    slightly more intuitive structure
    """
    response = {}

    try:
        response['count'] = int(results['d']['__count'])
    except:
        response['count'] = None

    if 'error' in results.keys():
        response['error'] = results['error']
        response['results'] = None
    elif type(results['d']) is list:
        response['results'] = results['d']
    elif 'results' in results['d'].keys():
        response['results'] = results['d']['results']
    else:
        response['results'] = results['d']

    return response


def get_related(response):
    """Make calls to the 'deferred'/related document
    types contained in the provided results object
    """
    deferred_urls = get_deferred_urls(response['results'])

    for entity, url in deferred_urls.items():
        r = requests.get(url + '?$format=json')
        related = r.json()
        response['results'][entity] = related['d']

    return response


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
