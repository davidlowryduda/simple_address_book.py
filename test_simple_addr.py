"""
Simple test suite.
"""

import os
import unittest

from simple_addr import AddressItem, AddressList

NAME1 = "Jim Bagodonuts"
EMAIL1 = "donutlover@test.com"
OTHERINFO1 = "loves donuts"

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
            _otherinfo     = OTHERINFO1
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


class TestAddressIO(unittest.TestCase):
    """
    Test file creation and reading.
    """
    def setUp(self):
        if os.path.isfile("tests"):
            raise IOError("tests is not a directory")
        if not os.path.exists("tests"):
            os.mkdir("tests")

    def tearDown(self):
        if os.path.exists('tests/addresses.test'):
            os.remove('tests/addresses.test')
        if os.path.isdir('tests'):
            os.rmdir('tests')

    def test_basic_write(self):
        """Create an addressfile with one item and read it."""
        alist = AddressList(filedir="tests", filename="addresses.test")
        alist.add_address(
            _name          = NAME1,
            _email_address = EMAIL1,
            _otherinfo     = OTHERINFO1
        )
        alist.write()
        self.assertTrue(os.path.exists('tests/addresses.test'))
        goal = "donutlover@test.com\tJim Bagodonuts\tloves donuts"
        with open('tests/addresses.test', 'r') as test_file:
            lines = test_file.readlines()
            self.assertEqual(lines[0].rstrip("\n"), goal)
            self.assertEqual(len(lines), 1)



def do_tests():
    """
    Run the test suite.
    """
    unittest.main(verbosity=2)


if __name__ == "__main__":
    do_tests()
