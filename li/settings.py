# API location info
API_SERVER = 'http://services.phila.gov/'
API_BASE = 'PhillyApi/Data/v0.7/Service.svc/'

# Default parameters applied to queries
# The API wants the parameters to start with
# a '$'. This library accepts them without the
# '$' (to make things simpler), then adds the
# '$' when creating the query string.
DEFAULT_PARAMS = {
    'format': 'json'  # Changing this to XML will break things
}

# Supported URL parameters that need to have a '$' prepended to them
QUERY_PARAMS = [
    #'expand',  # Expand currently breaks the API, so we'll disable it for now
    'filter',
    'format',
    'inlinecount',  # Can also use count=True, which is a little more intuitive
    'orderby',
    #'select',  # Disabled for now, unclear if it works
    'skip',
    'top',
]

# Document types supported by the API
DOC_TYPES = [
    'appealhearings',
    'buildingboardappeals',
    'cases',
    'hearingdates',
    'licenses',
    'licensedcontractors',
    'lireviewboardappeals',
    'locations',
    'permits',
    'violationdetails',
    'zoningboardappeals',
]

# Document types that don't want a singled-quoted doc_id
NUMBER_DOC_TYPE = [
    'locations',
    'buildingboardappeals',
    'appealhearings',
    'lireviewboardappeals',
    'violationdetails',
    'zoningboardappeals'
]
