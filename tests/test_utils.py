import unittest

from pycar_advanced import utils

class UtilsTestCase(unittest.TestCase):
    def test_slugify(self):
        """Test utils.slugify"""
        # It should:
        #
        # * Remove punctuation
        # * Lowercase characters
        # * Convert whitespace to a dash "-"
        self.assertEqual(utils.slugify("Cool string!"), "cool-string")

    def test_slugify_whitespace(self):    
        # TODO: slugify should also:
        #
        # * Remove leading/trailing whitespace
        # * Compact consecutive whitespace
        self.fail()
