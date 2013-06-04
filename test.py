import unittest

import li
from li.exceptions import DocTypeException, DocIDException


class LITestSequence(unittest.TestCase):

    def setup(self):
        pass

    def test_for_valid_document_id(self):
        """Tests that an invalid doc_id throws
        an exception
        """
        with self.assertRaises(DocIDException):
            li.get_license({'a': 'b'})

    def test_for_valid_document_type(self):
        """Tests that an invalid doc_type
        throws an exeception
        """
        with self.assertRaises(DocTypeException):
            li.get_documents('foo')

        with self.assertRaises(DocTypeException):
            li.get_document('foo', '000000')

    def test_get_appeal_hearing(self):
        """Returns details for a single appeal hearing
        """
        response = li.get_appeal_hearing('5')

        self.assertEqual(type(response['results']), dict)
        self.assertTrue('appeal_hearing_id' in response['results'].keys())

    def test_get_appeal_hearings(self):
        """Returns the first 1,000 most recent appeal hearings
        """
        response = li.get_appeal_hearings()

        self.assertEqual(type(response['results']), list)
        self.assertEqual(len(response['results']), 1000)

        for result in response['results']:
            self.assertTrue('appeal_hearing_id' in result.keys())

    def test_get_building_board_appeal(self):
        """Returns details for a single building board appeal
        """
        response = li.get_building_board_appeal('593403')

        self.assertEqual(type(response['results']), dict)
        self.assertTrue('appeal_id' in response['results'].keys())

    def test_get_building_board_appeals(self):
        """Returns the first 1,000 most building board appeals
        """
        response = li.get_building_board_appeals()

        self.assertEqual(type(response['results']), list)
        self.assertGreater(len(response['results']), 500)

        for result in response['results']:
            self.assertTrue('appeal_id' in result.keys())

    def test_get_case(self):
        """Returns details for a single case
        """
        response = li.get_case('0203312')

        self.assertEqual(type(response['results']), dict)
        self.assertTrue('case_number' in response['results'].keys())

    def test_get_cases(self):
        """Returns the first 1,000 most recent cases
        """
        response = li.get_cases()

        self.assertEqual(type(response['results']), list)
        self.assertEqual(len(response['results']), 1000)

        for result in response['results']:
            self.assertTrue('case_number' in result.keys())

    def test_get_contractor(self):
        """Returns details for a single contractor
        """
        response = li.get_contractor('10210')

        self.assertEqual(type(response['results']), dict)
        self.assertTrue('licensed_contractor_id' in response['results'].keys())

    def test_get_contractors(self):
        """Returns the first 1,000 licensed contractors
        """
        response = li.get_contractors()

        self.assertEqual(type(response['results']), list)
        self.assertEqual(len(response['results']), 1000)

        for result in response['results']:
            self.assertTrue('licensed_contractor_id' in result.keys())

    def test_get_hearing_date(self):
        """Returns details for a single hearing date
        """
        response = li.get_hearing_date('2009-04-29')

        self.assertEqual(type(response), dict)
        self.assertTrue('hearing_id' in response['results'].keys())

    def test_get_hearing_dates(self):
        """Returns the first 1,000 most recent licenses
        """
        response = li.get_hearing_dates()

        self.assertEqual(type(response['results']), list)
        self.assertEqual(len(response['results']), 1000)

        for result in response['results']:
            self.assertTrue('hearing_id' in result.keys())

    def test_get_license(self):
        """Returns details for a single license
        """
        response = li.get_license('015020')

        self.assertEqual(type(response['results']), dict)
        self.assertTrue('license_number' in response['results'].keys())

    def test_get_licenses(self):
        """Returns the first 1,000 most recent licenses
        """
        response = li.get_licenses()

        self.assertEqual(type(response['results']), list)
        self.assertEqual(len(response['results']), 1000)

        for result in response['results']:
            self.assertTrue('license_number' in result.keys())

    def test_get_location(self):
        """Returns details for a single location
        """
        response = li.get_location('333710')

        self.assertEqual(type(response['results']), dict)
        self.assertTrue('location_id' in response['results'].keys())

    def test_get_locations(self):
        """Returns the first 1,000 locations, ordered by location_id
        """
        response = li.get_locations()

        self.assertEqual(type(response['results']), list)
        self.assertEqual(len(response['results']), 1000)

        for result in response['results']:
            self.assertTrue('location_id' in result.keys())

    def test_get_li_review_board_appeal(self):
        """Returns details for a single li review board appeal
        """
        response = li.get_li_review_board_appeal('593634')

        self.assertEqual(type(response['results']), dict)
        self.assertTrue('appeal_id' in response['results'].keys())

    def test_get_li_review_board_appeals(self):
        """Returns the first 1,000 most recent li review board
        appeals
        """
        response = li.get_li_review_board_appeals()

        self.assertEqual(type(response['results']), list)
        self.assertEqual(len(response['results']), 1000)

        for result in response['results']:
            self.assertTrue('appeal_id' in result.keys())

    def test_get_permit(self):
        """Returns details for a single permit
        """
        response = li.get_permit('333274')

        self.assertEqual(type(response['results']), dict)
        self.assertTrue('permit_type_code' in response['results'].keys())

    def test_get_permits(self):
        """Returns the first 1,000 most recent permits
        """
        response = li.get_permits()

        self.assertEqual(type(response['results']), list)
        self.assertEqual(len(response['results']), 1000)

        for result in response['results']:
            self.assertTrue('permit_number' in result.keys())

    def test_get_violation(self):
        """Returns details for a single violation
        """
        response = li.get_violation('3941')

        self.assertEqual(type(response['results']), dict)
        self.assertTrue('violation_details_id' in response['results'].keys())

    def test_get_violations(self):
        """Returns the first 1,000 most recent violations
        """
        response = li.get_violations()

        self.assertEqual(type(response['results']), list)
        self.assertEqual(len(response['results']), 1000)

        for result in response['results']:
            self.assertTrue('violation_details_id' in result.keys())

    def test_get_zoning_board_appeal(self):
        """Returns details for a single zoning board appeal
        """
        response = li.get_zoning_board_appeal('593142')

        self.assertEqual(type(response['results']), dict)
        self.assertTrue('appeal_id' in response['results'].keys())

    def test_get_zoning_board_appeals(self):
        """Returns the first 1,000 most recent zoning board appeals
        """
        response = li.get_zoning_board_appeals()

        self.assertEqual(type(response['results']), list)
        self.assertEqual(len(response['results']), 1000)

        for result in response['results']:
            self.assertTrue('appeal_id' in result.keys())

    def test_get_permit_with_related(self):
        """Returns details for a specific permit,
        with the related documents retrieved
        """
        response = li.get_permit('333274', related=True)

        self.assertEqual(type(response['results']), dict)
        self.assertTrue('permit_type_code' in response['results'].keys())
        self.assertTrue('results' in response['results']['zoningboardappeals'].keys())
        self.assertTrue('street_name' in response['results']['locations'].keys())
        self.assertTrue('results' in response['results']['buildingboardappeals'].keys())

    def test_get_location_with_related(self):
        """Returns details for a specific locations,
        with the related documents retrieved
        """
        response = li.get_location('333710', related=True)

        self.assertEqual(type(response['results']), dict)
        self.assertTrue('location_id' in response['results'].keys())
        self.assertTrue('results' in response['results']['zoningboardappeals'].keys())
        self.assertTrue('results' in response['results']['lireviewboardappeals'].keys())
        self.assertTrue('results' in response['results']['buildingboardappeals'].keys())
        self.assertTrue('results' in response['results']['appealhearings'].keys())
        self.assertTrue('results' in response['results']['cases'].keys())
        self.assertTrue('results' in response['results']['permits'].keys())
        self.assertTrue('results' in response['results']['licenses'].keys())
        self.assertTrue('results' in response['results']['violationdetails'].keys())

    def test_get_licenses_with_related(self):
        """Returns details for a specific permit,
        with the related documents retrieved
        """
        response = li.get_license('015020', related=True)

        self.assertEqual(type(response['results']), dict)
        self.assertTrue('license_number' in response['results'].keys())
        self.assertTrue('street_name' in response['results']['locations'].keys())

    def test_get_permits_with_raw_sql_filter(self):
        """Allows the user to directly pass the $filter as
        as a ODATA SQL statement rather than passing a dict
        of params that is constructed into a ODATA SQL statement
        """
        sql = "application_type eq 'ZP_ZONING'"

        response = li.get_permits(filter=sql)

        for result in response['results']:
            self.assertEqual(result['application_type'], 'ZP_ZONING')

    def test_top_param(self):
        """The $top query parameter limits the request results
        to the number value of $top
        """
        response = li.get_permits(top=10)
        self.assertEqual(len(response['results']), 10)

        response = li.get_licenses(top=140)
        self.assertEqual(len(response['results']), 140)

        response = li.get_contractors(top=0)
        self.assertEqual(len(response['results']), 0)

    def test_inlinecount_query_param(self):
        """$inlinecount=allpages adds a '__count' key to the
        results with the total count of documents
        """
        response = li.get_permits(inlinecount='allpages')

        self.assertTrue(response['count'] is not None)

    def test_count_param_true(self):
        """Count is a convienent way to specify the
        $inlinecount query param with 'allpages' as the value
        """

        # if count is True, count should be set to a number
        response = li.get_permits(count=True)

        self.assertTrue(response['count'] is not None)
        self.assertTrue(type(response['count']) is int)

    def test_count_param_false(self):
        """Count is a convienent way to specify the
        $inlinecount query param with 'allpages' as the value
        """

        # if count is False, or not specified, the
        # return value of count should be None
        response = li.get_permits(count=False)

        self.assertTrue(response['count'] is None)

        response = li.get_permits()

        self.assertTrue(response['count'] is None)

    def test_api_error(self):
        """Passing a bogus query to the API should
        give us an error message stored at response['error']
        """
        sql = 'a bunch of stuff'

        response = li.get_permits(filter=sql)

        self.assertTrue('error' in response)


if __name__ == '__main__':
    unittest.main()
