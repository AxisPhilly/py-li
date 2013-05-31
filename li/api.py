import requests
from .utils import *


def get_permits(query_params):
    """Get the most recent permits, limited
    to 1,000 results by the API.
    Returns :list: of :dict:s

    :param query_params: :dict: of URL query parameters
    """
    url = construct_url('permits', query_params)

    r = requests.get(url)

    results = r.json()
    results = results['d']['results']

    return results


def get_permit(permit_id, related=False):
    """Get details for a specific permit
    """
    query_params = {}

    url = construct_url("permits('%s')" % permit_id, query_params)

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
