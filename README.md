#py-li

A thin Python wrapper for the City of Philadelphia [Licenses and Inspections API](http://phlapi.com/licenseapi.html).

### Installation

    pip install py-li

### Usage

The L&I API allows you to get details about L&I documents on a document by document basis, or in bulk. It's worth looking over the [documentation](http://phlapi.com/licenseapi.html) to see what document types and document details are available before diving in. Also, the API is based on Version 2.0 of the [ODATA API Protocol](http://www.odata.org/). The documentation is available [here](http://www.odata.org/documentation/odata-v2-documentation/uri-conventions/#Introduction). 

To get started, import the `py-li` library:

    >>> import li

The API is accessed through `li` by two types of methods: those that get multiple documents, and those that get a single document. Methods that retrieve multiple documents are plural, i.e. `get_permits`, `get_violations` and methods that retrieve a single document are singular, i.e. `get_permit`, `get_violation`.

**Multiple Documents**

The methods that return multiple documents accept the following parameters:

- **top**: (optional) Int or String. Limits the returned results to the set value. [ODATA documentation for $top](http://www.odata.org/documentation/odata-v2-documentation/uri-conventions/#43_Top_System_Query_Option_top).
- **filter**: (optional) String. An ODATA SQL *WHERE* statement. [ODATA documentation for $filter](http://www.odata.org/documentation/odata-v2-documentation/uri-conventions/#45_Filter_System_Query_Option_filter).
- **count**: (optional) Boolean. If set to `True`, the response will have a `count` key that holds the total number of documents available through the API for the requested document type. [ODATA documentation for $inlinecount](http://www.odata.org/documentation/odata-v2-documentation/uri-conventions/#49_Inlinecount_System_Query_Option_inlinecount)
- **skip**: (optional) Int or String. Skips X number of documents, and returns documents starting from there. [ODATA document for $skip](http://www.odata.org/documentation/odata-v2-documentation/uri-conventions/#44_Skip_System_Query_Option_skip)
- **orderby**: (optional) String. Sort the results by the provided field. [ODATA documentation for $orderby](http://www.odata.org/documentation/odata-v2-documentation/uri-conventions/#42_Orderby_System_Query_Option_orderby)

At the most basic level, you can easily retrieve permits (at the moment, a single bulk call to the API is limited to 1,000 documents), for instance, by doing the following:

    >>> response = li.get_permits()
    >>> response['results']
    [{u'status': u'COMPLETED', u'updated_datetime': u'/Date(1259076435000)/', u'application_type': u'BP_ALTER', u'locations': 
    {u'__deferred': {u'uri': u"http://services.phila.gov/PhillyAPI/Data/v0.7/Service.svc/permits('101930')/locations"}},
    u'issued_datetime': u'/Date(1194015498000)/', u'buildingboardappeals': {u'__deferred': {u'uri': u"http://services.phila
    gov/PhillyAPI/Data/v0.7/Service.svc/permits('101930')/buildingboardappeals"}}, u'pri_contact_first_name': u' ',
    u'pri_contact_address1': u'2023 W GIRARD AVE', u'pri_contact_address2': None, u'pri_contact_zip': u'19130', u'location_id': 71707,
    ...

Get the 1,000 most recent permits

    >>> response = li.get_permits(orderby='issued_datetime desc')

Passing `count=True`, which is a more convienent way to specify `inlinecount=allpages` query parameter, returns the total number of documents of the requested type that are available through the API:

    >>> response = li.get_permits(count=True)
    >>> len(response[results]) # number of results returned
    1000
    >>> response['count'] # total number of permits available through API
    273483

The `top` query parameter limits the number of results returned:

    >>> response = li.get_licenses(top=10)
    >>> len(response['results'])
    10

To receive a quick count of the total number of requested documents, use the `top` query parameter and `count=True`:

    >>> response = li.get_licenses(top=0, count=True)
    >>> len(response['results'])
    0
    >>> response['count']
    213881

Pass a [ODATA SQL](http://www.odata.org/documentation/odata-v2-documentation/uri-conventions/#45_Filter_System_Query_Option_filter) query as the filter parameter to get all the permits issued in 2013, for instance:

    >>> sql = "issued_datetime gt DateTime'2013-01-01'"
    >>> response = li.get_permits(filter=sql)

Get a count of the number of [CLIP](http://www.phila.gov/qualityoflife//index.html) violations issued in 2013:

    >>> sql = "violation_code eq 'CP-01' and violation_datetime gt DateTime'2013-01-01'"
    >>> response = li.get_violations(count=True, top=0, filter=sql)
    >>> response['count']
    5507

If you make a bad request, the error message from the API is passed along and stored at `response['error']`:

    >>> sql = "just new stuff"
    >>> response = li.get_licenses(filter=sql)
    >>> len(response['results'])
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: object of type 'NoneType' has no len()
    >>> response['error']
    {u'error': {u'message': {u'lang': u'en-US', u'value': u"No property 'just' exists in type 'Philagov.Data.PlanPhillyModel.licenses' at position 0."}, u'code': u''}}

**Single Document**

Once you've retrieved a set of documents, you have the information you need to start getting more details on a single document.

    >>> response = li.get_permits(orderby='issued_datetime desc')
    >>> response['results'][0]['permit_number']
    u'464771'
    >>> response = li.get_permit('464771', related=True)
    >>> response['results']
    {u'status': u'ACTIVE', u'updated_datetime': u'/Date(1370290469000)/', u'application_type': u'BP_NEWCNST', u'locations': 
    {u'council_district': u'04', u'zoningboardappeals': {u'__deferred': {u'uri': u'http://services.phila.gov/PhillyApi/Data/v0.
    7/Service.svc/locations(758962)/zoningboardappeals'}}, u'street_name': u'DRIFTWOOD', u'census_tract': u'027', 
    u'violationdetails': {u'__deferred': {u'uri': u'http://services.phila.gov/PhillyApi/Data/v0.7/Service.svc/locations(758962)
    /violationdetails'}}, u'licenses': {u'__deferred': {u'uri': u'http://services.phila.gov/PhillyApi/Data/v0.7/Service.svc/locations(
    758962)/licenses'}}, u'condo_unit': u'128', u'location_id': 758962, u'cases': {u'__deferred': {u'uri': u'http://services.phila.
    gov/PhillyApi/Data/v0.7/Service.svc/locations(758962)/cases'}}, u'city': u'PHILADELPHIA', u'zip': u'19129-1733',
    ...

By passing `related=True` in the above example, we tell `li` to retrieve the related documents for the requested document. The related documents for a permit are `locations`, `zoningboardappeals`, and `buildingboardappeals`. Without specifying `related=True`, the API returns does not get the details of the related documents, but instead returns a URL to get the details. For example:

    ...
        'pri_contact_type': 'APPLICANT',
        'zoningboardappeals': {
        '__deferred': {
            'uri': u"http://services.phila.gov/PhillyAPI/Data/v0.7/Service.svc/permits('464771')/zoningboardappeals"
          }
        },
        'permit_type_code': 'ENTIRE',
    ...

Methods that return a single document accept the following parameters:

- **doc_id**: String. The unique ID of the document you want to retrieve
- **related**: Boolean. If true, retrieves all documents related to the requested document.

See the examples folder and `test.py` for more usage examples.

### Contributing

Install the library:

1. Fork it
2. Install it: 
    
        cd py-li
        mkvirtualenv venv
        source venv/bin/activate
        pip install -r requirements.txt
        python test.py

3. Create your feature branch (`git checkout -b my-new-feature`)
4. Commit your changes (`git commit -am 'Added some feature'`)
5. Push to the branch (`git push origin my-new-feature`)
6. Create new pull Request

Make sure you added test cases for your feature!

### Copyright

Copyright © AxisPhilly. See LICENSE for details.
