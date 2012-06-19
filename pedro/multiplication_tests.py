#!/usr/bin/env python3

import unittest

from multiplication import mult


class TestMultiplication(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(mult(5, 6), 30)

    def test_double_digits(self):
        self.assertEqual(mult(12, 34), 408)

    def test_same_multiple_digits(self):
        self.assertEqual(mult(1234, 5678), 7006652)

if __name__ == '__main__':
    unittest.main()
