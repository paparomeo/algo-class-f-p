#!/usr/bin/env python3

import unittest

from multiplication import multiplication


class TestMultiplication(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(multiplication('5', '6'), '30')

    def test_double_digits_exception(self):
        self.assertRaises(ValueError, multiplication, '12', '34')

if __name__ == '__main__':
    unittest.main()
