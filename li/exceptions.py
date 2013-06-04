class LIException(Exception):
    """There was an ambiguous exception that occurred while handling your
    request."""


class DocTypeException(LIException):
    """The provided document type is invalid.
    """


class DocIDException(LIException):
    """The provided document ID is invalid.
    """
