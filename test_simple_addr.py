"""
Simple test suite.
"""

import unittest

from simple_addr import AddressItem

NAME1 = "Jim Bagodonuts"
EMAIL1 = "donutlover@test.com"

NAME2 = "Janet Bucketochips"
EMAIL2 = "crunchy@test.com"


class TestAddressItem(unittest.TestCase):
    """
    Test basic properties of an AddressItem.
    """
    def setUp(self):
        self.aditem1 = AddressItem(
            _email_address = EMAIL1,
            _name          = NAME1,
            _otherinfo     = "loves donuts"
        )
        self.aditem2 = AddressItem(
            _email_address = EMAIL2,
            _name          = NAME2
        )

    def tearDown(self):
        self.aditem = None
        self.aditem2 = None

    def test_string_rep(self):
        """
        Test creating an item and its string representation.
        """
        goal1 = "donutlover@test.com\tJim Bagodonuts\tloves donuts"
        goal2 = "crunchy@test.com\tJanet Bucketochips\t"
        self.assertEqual(str(self.aditem1), goal1)
        self.assertEqual(str(self.aditem2), goal2)

def do_tests():
    """
    Run the test suite.
    """
    unittest.main(verbosity=2)


if __name__ == "__main__":
    do_tests()
