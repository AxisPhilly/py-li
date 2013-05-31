import li
import unittest


class LIAPITestSequence(unittest.TestCase):

    def setup(self):
        pass

    def test_get_permits(self):
        """Returns the first 1,000 most recent permits as a list/JSON
        """
        results = li.get_permits({})

        self.assertEqual(type(results), list)
        self.assertEqual(len(results), 1000)

    def test_get_permit(self):
        """Returns details for a single permit
        """
        results = li.get_permit(333274)

        self.assertEqual(type(results), dict)
        self.assertTrue('permit_type_code' in results.keys())

    def test_get_permit_with_related(self):
        """Returns details for a specific permit
        """
        results = li.get_permit(333274, related=True)

        self.assertEqual(type(results), dict)
        self.assertTrue('permit_type_code' in results.keys())
        self.assertTrue('results' in results['zoningboardappeals'].keys())
        self.assertTrue('street_name' in results['locations'].keys())
        self.assertTrue('results' in results['buildingboardappeals'].keys())


if __name__ == '__main__':
    unittest.main()
