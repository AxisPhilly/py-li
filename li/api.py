from .utils import *
import requests


def get_document(doc_type, doc_id, related=False):
    """Invoke a call to the API for a single document
    """
    if doc_type != 'locations':
        doc_id = "\'" + doc_id + "\'"

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
    """Invoke a call to the API for multiple documents
    """
    url = construct_url(doc_type, query_params, sql)

    r = requests.get(url)

    results = r.json()
    results = results['d']['results']

    return results
