import li
from li.utils import LIException
import unittest


class LIAPITestSequence(unittest.TestCase):

    def setup(self):
        pass

    def test_for_doc_id_for_get_document(self):
        """Functions that retrieve singular documents
        require the ID parameter
        """
        with self.assertRaises(TypeError):
            li.get_license({'a': 'b'})

    def test_for_valid_document_type(self):
        """Tests that the provided document type is
        valid
        TODO: Can't this just be LIException instead of 
        li.utils.LIException
        """
        with self.assertRaises(li.utils.LIException):
            li.get_documents('foo')

        with self.assertRaises(li.utils.LIException):
            li.get_document('foo', '000000')

    def test_get_appeal_hearing(self):
        """Returns details for a single appeal hearing
        """
        results = li.get_appeal_hearing('5')

        self.assertEqual(type(results), dict)
        self.assertTrue('appeal_hearing_id' in results.keys())

    def test_get_appeal_hearings(self):
        """Returns the first 1,000 most recent appeal hearings
        """
        results = li.get_appeal_hearings()

        self.assertEqual(type(results), list)
        self.assertEqual(len(results), 1000)

        for result in results:
            self.assertTrue('appeal_hearing_id' in result.keys())

    def test_get_building_board_appeal(self):
        """Returns details for a single building board appeal
        """
        results = li.get_building_board_appeal('593403')

        self.assertEqual(type(results), dict)
        self.assertTrue('appeal_id' in results.keys())


    def test_get_building_board_appeals(self):
        """Returns the first 1,000 most building board appeals
        """
        results = li.get_building_board_appeals()

        self.assertEqual(type(results), list)
        self.assertGreater(len(results), 500)

        for result in results:
            self.assertTrue('appeal_id' in result.keys())

    def test_get_case(self):
        """Returns details for a single case
        """
        results = li.get_case('0203312')

        self.assertEqual(type(results), dict)
        self.assertTrue('case_number' in results.keys())

    def test_get_cases(self):
        """Returns the first 1,000 most recent cases
        """
        results = li.get_cases()

        self.assertEqual(type(results), list)
        self.assertEqual(len(results), 1000)

        for result in results:
            self.assertTrue('case_number' in result.keys())

    def test_get_contractor(self):
        """Returns details for a single contractor
        """
        results = li.get_contractor('10210')

        self.assertEqual(type(results), dict)
        self.assertTrue('licensed_contractor_id' in results.keys())

    def test_get_contractors(self):
        """Returns the first 1,000 licensed contractors
        """
        results = li.get_contractors()

        self.assertEqual(type(results), list)
        self.assertEqual(len(results), 1000)

        for result in results:
            self.assertTrue('licensed_contractor_id' in result.keys())

    def test_get_hearing_date(self):
        """Returns details for a single hearing date
        """
        results = li.get_hearing_date('2009-04-29')

        self.assertEqual(type(results), dict)
        self.assertTrue('hearing_id' in results.keys())

    def test_get_hearing_dates(self):
        """Returns the first 1,000 most recent licenses
        """
        results = li.get_hearing_dates()

        self.assertEqual(type(results), list)
        self.assertEqual(len(results), 1000)

        for result in results:
            self.assertTrue('hearing_id' in result.keys())

    def test_get_license(self):
        """Returns details for a single license
        """
        results = li.get_license('015020')

        self.assertEqual(type(results), dict)
        self.assertTrue('license_number' in results.keys())

    def test_get_licenses(self):
        """Returns the first 1,000 most recent licenses
        """
        results = li.get_licenses()

        self.assertEqual(type(results), list)
        self.assertEqual(len(results), 1000)

        for result in results:
            self.assertTrue('license_number' in result.keys())

    def test_get_location(self):
        """Returns details for a single location
        """
        results = li.get_location('333710')

        self.assertEqual(type(results), dict)
        self.assertTrue('location_id' in results.keys())

    def test_get_locations(self):
        """Returns the first 1,000 locations, ordered by location_id
        """
        results = li.get_locations()

        self.assertEqual(type(results), list)
        self.assertEqual(len(results), 1000)

        for result in results:
            self.assertTrue('location_id' in result.keys())

    def test_get_li_review_board_appeal(self):
        """Returns details for a single li review board appeal
        """
        results = li.get_li_review_board_appeal('593634')

        self.assertEqual(type(results), dict)
        self.assertTrue('appeal_id' in results.keys())

    def test_get_li_review_board_appeals(self):
        """Returns the first 1,000 most recent li review board
        appeals
        """
        results = li.get_li_review_board_appeals()

        self.assertEqual(type(results), list)
        self.assertEqual(len(results), 1000)

        for result in results:
            self.assertTrue('appeal_id' in result.keys())

    def test_get_permit(self):
        """Returns details for a single permit
        """
        results = li.get_permit('333274')

        self.assertEqual(type(results), dict)
        self.assertTrue('permit_type_code' in results.keys())

    def test_get_permits(self):
        """Returns the first 1,000 most recent permits
        """
        results = li.get_permits()

        self.assertEqual(type(results), list)
        self.assertEqual(len(results), 1000)

        for result in results:
            self.assertTrue('permit_number' in result.keys())

    def test_get_violation(self):
        """Returns details for a single violation
        """
        results = li.get_violation('3941')

        self.assertEqual(type(results), dict)
        self.assertTrue('violation_details_id' in results.keys())

    def test_get_violations(self):
        """Returns the first 1,000 most recent violations
        """
        results = li.get_violations()

        self.assertEqual(type(results), list)
        self.assertEqual(len(results), 1000)

        for result in results:
            self.assertTrue('violation_details_id' in result.keys())

    def test_get_zoning_board_appeal(self):
        """Returns details for a single zoning board appeal
        """
        results = li.get_zoning_board_appeal('593142')

        self.assertEqual(type(results), dict)
        self.assertTrue('appeal_id' in results.keys())

    def test_get_zoning_board_appeals(self):
        """Returns the first 1,000 most recent zoning board appeals
        """
        results = li.get_zoning_board_appeals()

        self.assertEqual(type(results), list)
        self.assertEqual(len(results), 1000)

        for result in results:
            self.assertTrue('appeal_id' in result.keys())

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

        results = li.get_permits(sql=sql)

        for result in results:
            self.assertEqual(result['application_type'], 'ZP_ZONING')

if __name__ == '__main__':
    unittest.main()
