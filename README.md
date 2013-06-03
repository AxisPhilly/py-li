#py-li

A thin Python wrapper for the City of Philadelphia [Licenses and Inspections API](http://phlapi.com/licenseapi.html)

## Installation

Users:

    pip install py-li

Developers:

    git clone git://github.com/axisphilly/py-li.git
    cd py-li
    mkvirtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python test.py

## Usage

    import li

Get the 1,000 most recent permits

    li.get_permits()

    [
      {
        'status': 'COMPLETED',
        'updated_datetime': '/Date(1259076435000)/',
        'application_type': 'BP_ALTER',
        'locations': {
            '__deferred': {
                'uri': u"http://services.phila.gov/PhillyAPI/Data/v0.7/Service.svc/permits('101930')/locations"
            }
        },
        'issued_datetime': '/Date(1194015498000)/',
        'buildingboardappeals': {
            '__deferred': {
                'uri': u"http://services.phila.gov/PhillyAPI/Data/v0.7/Service.svc/permits('101930')/buildingboardappeals"
            }
        },
        'pri_contact_first_name': '',
        'pri_contact_address1': '2023WGIRARDAVE',
        'pri_contact_address2': None,
        'pri_contact_zip': '19130',
        'location_id': 71707,
        'pri_contact_type': 'OWNER',
        'zoningboardappeals': {
            '__deferred': {
                'uri': u"http://services.phila.gov/PhillyAPI/Data/v0.7/Service.svc/permits('101930')/zoningboardappeals"
            }
        },
        'permit_type_code': 'MAJOR',
        'pri_contact_state': None,
        'work_description': 'RENOVATIONSFORBUSINESSANDAPARTMENTS.',
        'pri_contact_city': 'PHILADELPHIAPA',
        'permit_type_name': 'ALT-MAJORALTERATION',
        'pri_contact_last_name': 'OSUAGWUNNAMDISHANKSDAVID',
        'contractor_city': 'PHILADELPHIA,
        ',
        'contractor_name': 'SENSIBLEDEVELOPMENTSLLC',
        'contractor_address2': None,
        'contractor_address1': '1008SOUTH5THSTREET',
        'application_description': 'ALTERATIONPERMIT',
        '__metadata': {
            'type': 'PlanPhillyModel.permits',
            'uri': u"http://services.phila.gov/PhillyAPI/Data/v0.7/Service.svc/permits('101930')"
        },
        'pri_contact_company_name': None,
        'contractor_state': 'PA',
        'permit_number': '101930',
        'contractor_zip': '19147'
      },
    ...
    ]


See the examples folder and `test.py` for more usage examples.

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Added some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new pull Request

Make sure you added test cases for your feature!

## Copyright

Copyright © AxisPhilly. See LICENSE for details.
