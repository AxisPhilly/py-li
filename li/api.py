from .utils import *


def get_document(doc_type, doc_id, **kwargs):
    """
    Invoke a GET request to the API for a single document.

    Returns a dict with details of the document available
    at the 'results' key

    :doc_type: String. Contains the type of document to retrieve.
    :doc_id: String. Unique identifier for document.
    :related: Boolean. Indicates if related documents should be retrieved.
    """
    # Make sure the provided doc_type is a valid doc_type
    validate_doc_type(doc_type)

    # Add single quotes to doc_id if necessary
    doc_id = validate_doc_id(doc_id, doc_type)

    # Build the API URL to request
    url = construct_url("%s(%s)" % (doc_type, doc_id), **kwargs)

    # Make a call to the API with the provided URL
    response = invoke_api(url)

    # the $expand parameters results in bad responses
    # so we get each primary deferred/related entity
    # by making a making a request to the supplied url
    if 'related' in kwargs and kwargs['related'] is True:
        response = get_related(response)

    return response


def get_documents(doc_type, **kwargs):
    """
    Invoke a GET request to the API for a set of documents.

    Returns a dict with following keys:
        results: list of documents with their details
        count: if count=True, count of total documents
        error: dict with error information passed along from API response

    :top: (optional) Int or String. Limits the returned results to the set value.
    :filter: (optional) String. An ODATA SQL *WHERE* statement.
    :count: (optional) Boolean. If set to `True`, the response will have a `count` key that
                        holds the total number of documents available through the API for
                        the requested document type.
    :skip: (optional) Int or String. Skips X number of documents, and returns
                        documents starting from there.
    :orderby: (optiona) String. Sort the results by the provided field.
    """
    # Make sure the provided doc_type is a valid doc_type
    validate_doc_type(doc_type)

    # Make sure the keys in query_params are valid
    #validate_query_params(query_params)

    # Build the API URL to request
    url = construct_url(doc_type, **kwargs)

    # Make a call to the API with the provided URL
    response = invoke_api(url)

    return response


# Convience functions to get a single or multiples documents
# for each document type supported by the API.
# In alphabetical order by document type:

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
