#!/usr/bin/env python3

import random
import unittest

from mergesort import merge, merge_sort


class TestMergeSort(unittest.TestCase):

    def test_merge_trivial_1(self):
        self.assertEqual(merge([], []), [])

    def test_merge_trivial_1(self):
        self.assertEqual(merge([], [1]), [1])

    def test_merge_trivial_1(self):
        self.assertEqual(merge([1], []), [1])

    def test_merge_trivial_1(self):
        self.assertEqual(merge([2], [1]), [1, 2])

    def test_merge_balanced(self):
        self.assertEqual(merge([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])

    def test_merge_unbalanced(self):
        self.assertEqual(merge([1, 3, 5], [4]), [1, 3, 4, 5])

    def test_merge_sort(self):
        sorted_numbers = list(range(1000000))
        shuffled_numbers = sorted_numbers[:]
        random.shuffle(shuffled_numbers)
        self.assertEqual(merge_sort(shuffled_numbers), sorted_numbers)

if __name__ == '__main__':
    unittest.main()
