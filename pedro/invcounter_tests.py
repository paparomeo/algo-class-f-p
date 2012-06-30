#!/usr/bin/env python3

import random
import unittest

from invcounter import merge_and_count_inv, sort_and_count_inv


class TestMergeSort(unittest.TestCase):

    def test_merge_and_count_inv_1(self):
        self.assertEqual(merge_and_count_inv((0, []), (0, [])), (0, []))

    def test_merge_and_count_inv_2(self):
        self.assertEqual(merge_and_count_inv((0, []), (0, [1])), (0, [1]))

    def test_merge_and_count_inv_3(self):
        self.assertEqual(merge_and_count_inv((0, [1]), (0, [])), (0, [1]))

    def test_merge_and_count_inv_4(self):
        self.assertEqual(merge_and_count_inv((0, [1]), (0, [2])), (0, [1, 2]))

    def test_merge_and_count_inv_5(self):
        self.assertEqual(merge_and_count_inv((0, [2]), (0, [1])), (1, [1, 2]))

    def test_merge_and_count_inv_6(self):
        self.assertEqual(merge_and_count_inv((0, [1, 2]), (0, [3, 4])),
                         (0, [1, 2, 3, 4]))

    def test_merge_and_count_inv_6(self):
        self.assertEqual(merge_and_count_inv((0, [3, 4]), (0, [1, 2])),
                         (4, [1, 2, 3, 4]))

    def test_sort_and_count_inv_1(self):
        self.assertEqual(sort_and_count_inv([]), (0, []))

    def test_sort_and_count_inv_2(self):
        self.assertEqual(sort_and_count_inv([1]), (0, [1]))

    def test_sort_and_count_inv_3(self):
        self.assertEqual(sort_and_count_inv([1, 2]), (0, [1, 2]))

    def test_sort_and_count_inv_4(self):
        self.assertEqual(sort_and_count_inv([2, 1]), (1, [1, 2]))

    def test_sort_and_count_inv_5(self):
        self.assertEqual(sort_and_count_inv([6, 5, 4, 3, 2, 1]),
                         (15, [1, 2, 3, 4, 5, 6]))

if __name__ == '__main__':
    unittest.main()
