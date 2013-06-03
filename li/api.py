from .utils import *


def get_document(doc_type, doc_id, related=False):
    """
    Invoke a GET request to the API for a single document

    :doc_type: String containing the type of document to retrieve.
    :ID: String unique identifier for document. Required when requesting single document.
    :related: Boolean indicating if related documents should be retrieved.
    """
    # Make sure the provided doc_type is a valid doc_type
    validate_doc_type(doc_type)

    # Add single quotes to doc_id if necessary
    doc_id = validate_doc_id(doc_id, doc_type)

    # Build the API URL to request
    url = construct_url("%s(%s)" % (doc_type, doc_id), {}, None)

    # Make a call to the API with the provided URL
    results = invoke_api(url)

    # the $expand parameters results in bad responses
    # so we get each primary deferred/related entity
    # by making a making a request to the supplied url
    if related:
        results = get_related(results)

    return results


def get_documents(doc_type, query_params={}, sql=None):
    """
    Invoke a GET request to the API for a set of documents

    :doc_type: String containing the type of document to retrieve.
    :query_params: (optional) Dictionary with accepted query parameters. TODO: Check for accepted parameters
    :sql: (optional) String containing ODATA SQL statement for $filter parameter.
            Only used when retrieving multiple documents.
    """
    validate_doc_type(doc_type)

    url = construct_url(doc_type, query_params, sql)

    results = invoke_api(url)

    return results


# Convience functions to get a single or multiples documents
# for each document type supported by the API
# In alphabetical order by document type

def get_appeal_hearing(doc_id, **kwargs):

    return get_document('appealhearings', doc_id, **kwargs)


def get_appeal_hearings(**kwargs):

    return get_documents('appealhearings', **kwargs)


def get_building_board_appeal(doc_id, **kwargs):

    return get_document('buildingboardappeals', doc_id, **kwargs)


def get_building_board_appeals(**kwargs):

    return get_documents('buildingboardappeals', **kwargs)


def get_case(doc_id, **kwargs):

    return get_document('cases', doc_id, **kwargs)


def get_cases(**kwargs):

    return get_documents('cases', **kwargs)


def get_contractor(doc_id, **kwargs):

    return get_document('licensedcontractors', doc_id, **kwargs)


def get_contractors(**kwargs):

    return get_documents('licensedcontractors', **kwargs)


def get_hearing_date(doc_id, **kwargs):

    return get_document('hearingdates', doc_id, **kwargs)


def get_hearing_dates(**kwargs):

    return get_documents('hearingdates', **kwargs)


def get_license(doc_id, **kwargs):

    return get_document('licenses', doc_id, **kwargs)


def get_licenses(**kwargs):

    return get_documents('licenses', **kwargs)


def get_location(doc_id, **kwargs):

    return get_document('locations', doc_id, **kwargs)


def get_locations(**kwargs):

    return get_documents('locations', **kwargs)


def get_li_review_board_appeal(doc_id, **kwargs):

    return get_document('lireviewboardappeals', doc_id, **kwargs)


def get_li_review_board_appeals(**kwargs):

    return get_documents('lireviewboardappeals', **kwargs)


def get_permit(doc_id, **kwargs):

    return get_document('permits', doc_id, **kwargs)


def get_permits(**kwargs):

    return get_documents('permits', **kwargs)


def get_violation(doc_id, **kwargs):

    return get_document('violationdetails', doc_id, **kwargs)


def get_violations(**kwargs):

    return get_documents('violationdetails', **kwargs)


def get_zoning_board_appeal(doc_id, **kwargs):

    return get_document('zoningboardappeals', doc_id, **kwargs)


def get_zoning_board_appeals(**kwargs):

    return get_documents('zoningboardappeals', **kwargs)
