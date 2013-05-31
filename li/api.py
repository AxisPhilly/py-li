from .utils import *
import requests


def get_document(doc_type, doc_id, related=False):
    """
    Invoke a GET request to the API for a single document

    :doc_type: String containing the type of document to retrieve.
    :ID: String unique identifier for document. Required when requesting single document.
    :related: Boolean indicating if related documents should be retrieved. 
    """
    check_doc_type(doc_type)

    if doc_type != 'locations':
        try:
            doc_id = "\'" + doc_id + "\'"
        except:
            raise TypeError('The first parameter must be the document id and a string')

    url = construct_url("%s(%s)" % (doc_type, doc_id), {}, None)

    r = requests.get(url)
    results = r.json()
    results = results['d']

    # the $expand parameters results in bad responses
    # so we get each primary deferred/related entity
    # by making a making a request to the supplied url
    if related:
        deferred_urls = get_deferred_urls(results)

        for entity, url in deferred_urls.items():
            r = requests.get(url + '?$format=json')
            related = r.json()
            results[entity] = related['d']

    return results


def get_documents(doc_type, query_params={}, sql=None):
    """
    Invoke a GET request to the API for a set of documents

    :doc_type: String containing the type of document to retrieve.
    :query_params: (optional) Dictionary with accepted query parameters. TODO: Check for accepted parameters
    :sql: (optional) String containing ODATA SQL statement for $filter parameter.
            Only used when retrieving multiple documents.
    """
    check_doc_type(doc_type)

    url = construct_url(doc_type, query_params, sql)

    r = requests.get(url)
    results = r.json()
    results = results['d']['results']

    return results


def get_permit(doc_id, **kwargs):

    return get_document('permits', doc_id, **kwargs)


def get_permits(**kwargs):

    return get_documents('permits', **kwargs)


def get_location(doc_id, **kwargs):

    return get_document('locations', doc_id, **kwargs)


def get_locations(**kwargs):

    return get_documents('locations', **kwargs)


def get_license(doc_id, **kwargs):

    return get_document('licenses', doc_id, **kwargs)


def get_licenses(**kwargs):

    return get_documents('licenses', **kwargs)
