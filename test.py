import li
import unittest


class LIAPITestSequence(unittest.TestCase):

    def setup(self):
        pass

    def test_get_permits(self):
        """Returns the first 1,000 most recent permits
        """
        results = li.get_permits({})

        self.assertEqual(type(results), list)
        self.assertEqual(len(results), 1000)

        for result in results:
            self.assertTrue('permit_number' in result.keys())

    def test_get_locations(self):
        """Returns the first 1,000 locations, ordered by location_id
        """
        results = li.get_locations({})

        self.assertEqual(type(results), list)
        self.assertEqual(len(results), 1000)

        for result in results:
            self.assertTrue('location_id' in result.keys())

    def test_get_licenses(self):
        """Returns the first 1,000 most recent licenses
        """
        results = li.get_licenses({})

        self.assertEqual(type(results), list)
        self.assertEqual(len(results), 1000)

        for result in results:
            self.assertTrue('license_number' in result.keys())

    def test_get_permit(self):
        """Returns details for a single permit
        """
        results = li.get_permit('333274')

        self.assertEqual(type(results), dict)
        self.assertTrue('permit_type_code' in results.keys())

    def test_get_location(self):
        """Returns details for a single location
        """
        results = li.get_location('333710')

        self.assertEqual(type(results), dict)
        self.assertTrue('location_id' in results.keys())

    def test_get_license(self):
        """Returns details for a single license
        """
        results = li.get_license('015020')

        self.assertEqual(type(results), dict)
        self.assertTrue('license_number' in results.keys())

    def test_get_permit_with_related(self):
        """Returns details for a specific permit,
        with the related documents retrieved
        """
        results = li.get_permit('333274', related=True)

        self.assertEqual(type(results), dict)
        self.assertTrue('permit_type_code' in results.keys())
        self.assertTrue('results' in results['zoningboardappeals'].keys())
        self.assertTrue('street_name' in results['locations'].keys())
        self.assertTrue('results' in results['buildingboardappeals'].keys())

    def test_get_location_with_related(self):
        """Returns details for a specific locations,
        with the related documents retrieved
        """
        results = li.get_location('333710', related=True)

        self.assertEqual(type(results), dict)
        self.assertTrue('location_id' in results.keys())
        self.assertTrue('results' in results['zoningboardappeals'].keys())
        self.assertTrue('results' in results['lireviewboardappeals'].keys())
        self.assertTrue('results' in results['buildingboardappeals'].keys())
        self.assertTrue('results' in results['appealhearings'].keys())
        self.assertTrue('results' in results['cases'].keys())
        self.assertTrue('results' in results['permits'].keys())
        self.assertTrue('results' in results['licenses'].keys())
        self.assertTrue('results' in results['violationdetails'].keys())

    def test_get_licenses_with_related(self):
        """Returns details for a specific permit,
        with the related documents retrieved
        """
        results = li.get_license('015020', related=True)

        self.assertEqual(type(results), dict)
        self.assertTrue('license_number' in results.keys())
        self.assertTrue('street_name' in results['locations'].keys())

    def test_get_permits_with_raw_sql_filter(self):
        """Allows the user to directly pass the $filter as
        as a ODATA SQL statement rather than passing a dict
        of params that is constructed into a ODATA SQL statement
        """
        sql = "application_type eq 'ZP_ZONING'"

        results = li.get_permits({}, sql=sql)

        for result in results:
            self.assertEqual(result['application_type'], 'ZP_ZONING')

if __name__ == '__main__':
    unittest.main()
