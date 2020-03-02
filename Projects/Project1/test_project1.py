import unittest

from project1 import add, subtract, divide, multiply


class TestProject1(unittest.TestCase):

    def test_add_1(self):
        self.assertEqual(add(10, 10), 20)

    def test_add_2(self):
        self.assertEqual(add(-10, 10), 0)

    def test_add_3(self):
        self.assertEqual(add(10, -10), 0)

    def test_add_4(self):
        self.assertEqual(add(-10, 20), 10)

    def test_add_5(self):
        self.assertEqual(add(10, -50), -40)

    def test_subtract_1(self):
        self.assertEqual(subtract(10, 10), 0)

    def test_subtract_2(self):
        self.assertEqual(subtract(-10, 10), -20)

    def test_subtract_3(self):
        self.assertEqual(subtract(10, -10), 20)

    def test_subtract_4(self):
        self.assertEqual(subtract(-10, -10), 0)

    def test_divide_1(self):
        self.assertEqual(divide(10, 10), 1)

    def test_divide_2(self):
        self.assertEqual(divide(-10, 10), -1)

    def test_divide_3(self):
        self.assertEqual(divide(10, -10), -1)

    def test_divide_4(self):
        self.assertEqual(divide(0, 10), 0)

    def test_divide_5(self):
        self.assertEqual(divide(10, 0), str)


unittest.main()
