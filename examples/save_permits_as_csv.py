import sys
sys.path.append("..")
import li
import csv
import codecs
import cStringIO


class DictUnicodeWriter(object):
    """Unicode CSV writer from
    http://stackoverflow.com/questions/5838605/python-dictwriter-writing-utf-8-encoded-csv-files
    """

    def __init__(self, f, fieldnames, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.DictWriter(self.queue, fieldnames, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, D):
        self.writer.writerow({k: v.encode("utf-8", 'replace') for k, v in D.items()})
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8", 'replace')
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data, 'replace')
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for D in rows:
            self.writerow(D)

    def writeheader(self):
        self.writer.writeheader()


# Get the 1,000 most recent permits
response = li.get_permits()

"""
The related attributes are currently dicts that have
the following structure:

    'buildingboardappeals': {
        '__deferred': {
            'uri': u"http://services.phila.gov/PhillyAPI/Data/v0.7/Service.svc/permits('/')/buildingboardappeals"
        }
    }

For the purposes of writing a csv, we'll pull out the uri value
and set that has the value of buildingboardappeals, because can't
write a dictionary to CSV, the url is the valuable part anyway
"""

for permit in response['results']:
    permit['buildingboardappeals'] = permit['buildingboardappeals']['__deferred']['uri']
    permit['locations'] = permit['locations']['__deferred']['uri']
    permit['zoningboardappeals'] = permit['zoningboardappeals']['__deferred']['uri']
    permit['__metadata'] = permit['__metadata']['uri']

    # Also, we need to clean up None and Ints so we can encode them to unicode
    for k, v in permit.items():
        if v is None:
            permit[k] = u'null'

        if isinstance(v, int) is True:
            permit[k] = str(v)


with open('permits.csv', 'wb') as f:
    # write header row
    dict_writer = DictUnicodeWriter(f, response['results'][0].keys())
    dict_writer.writeheader()

    # write permits
    dict_writer.writerows(response['results'])
