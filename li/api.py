from .utils import *


def get_permits(query_params, sql=None):
    """Get the most recent permits, limited
    to 1,000 results by the API.
    Returns :list: of :dict:s

    :param query_params: :dict: of URL query parameters
    :sql: string with ODATA SQL query for $filter param
    """
    results = get_documents('permits', query_params, sql)

    return results


def get_locations(query_params, sql=None):
    """Get locations ordered by location_id
    limited to 1,000 results by the API.
    Returns :list: of :dict:s

    :param query_params: :dict: of URL query parameters
    :sql: string with ODATA SQL query for $filter param
    """
    results = get_documents('locations', query_params, sql)

    return results


def get_permit(permit_id, related=False):
    """Get details for a specific permit
    """
    results = get_document('permits', permit_id)

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


def get_location(location_id, related=False):
    """Get details for a specific location
    """
    results = get_document('locations', location_id)

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

def get_licenses(query_params, sql=None):
    """Get the most recent licenses, limited
    to 1,000 results by the API.
    Returns :list: of :dict:s

    :param query_params: :dict: of URL query parameters
    :sql: string with ODATA SQL query for $filter param
    """
    results = get_documents('licenses', query_params, sql)

    return results

def get_license(license_id, related=False):
    """Get details for a specific license
    """
    results = get_document('licenses', license_id)

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
