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
    self.assertTrue(results.has_key('permit_type_code'))

  def test_get_permit_with_related(self):
    """Returns details for a specific permit
    """
    results = li.get_permit(333274, related=True)
    
    self.assertEqual(type(results), dict)
    self.assertTrue(results.has_key('permit_type_code'))
    self.assertTrue(results['zoningboardappeals'].has_key('results'))
    self.assertTrue(results['locations'].has_key('street_name'))
    self.assertTrue(results['buildingboardappeals'].has_key('results'))

if __name__ == '__main__':
    unittest.main()
