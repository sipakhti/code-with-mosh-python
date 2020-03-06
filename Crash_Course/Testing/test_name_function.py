import unittest

from name_function import formatted_name


class TestNameFunction(unittest.TestCase):
    """tests for formatted_name()"""

    def test_first_last_name_1(self):
        """ do names like 'Umer Mehmood' Work"""
        test_name = formatted_name("Umer", "Mehmood")
        self.assertEqual(test_name, "Umer Mehmood")

    def test_first_last_middle_1(self):
        """ Do name like Umer Mehmood Khan Work"""
        test_name = formatted_name("Umer", "khan", "mehmood")
        self.assertEqual(test_name, "Umer Mehmood Khan")


unittest.main()
