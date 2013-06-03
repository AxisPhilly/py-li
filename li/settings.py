# API location info
API_SERVER = 'http://services.phila.gov/'
API_BASE = 'PhillyApi/Data/v0.7/Service.svc/'

# Default parameters applied to queries
DEFAULT_PARAMS = {
    '$format': 'json'  # Changing this to XML will break things
}

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
