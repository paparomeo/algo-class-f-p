# encoding:utf-8
import unittest

from quicksort import quicksort


class QuickSortTest(unittest.TestCase):
    """
    Tests the quicksort algorithm
    """
    def test_partition_1(self):
        array = [3, 5, 1, 4, 2, 6]
        left = [2, 1]
        right = [4, 5, 6]

    def test_partition_2(self):
        array = [3, 8, 2, 5, 1, 4, 7, 6]
        left = [1, 2]
        right = [5, 8, 4, 7, 6]

    def test_sort_basic(self):
        array = [1]
        ordered = [1]
        self.assertEquals(quicksort(array), ordered)
        
    def test_sort_basic_2(self):
        array = [3, 1]
        ordered = [1, 3]
        self.assertEquals(quicksort(array), ordered)
        
    def test_sort_4(self):
        array = [3, 1, 2, 4]
        ordered = [1, 2, 3, 4]
        self.assertEquals(quicksort(array), ordered)

    #def test_sort_lesson_example(self):
    #    array = [1, 3, 5, 2, 4, 6]
    #    ordered = [1, 2, 3, 4, 5, 6]
    #    self.assertEquals(mergesort(array), ordered)

    #def test_sort_max(self):
    #    array = [6, 5, 4, 3, 2, 1]
    #    ordered = [1, 2, 3, 4, 5, 6]
    #    self.assertEquals(quicksort(array), ordered)

    #def test_exercise(self):
    #    with open('QuickSort.txt') as f:
    #        array = [int(line.strip()) for line in f.readlines()]
    #        quicksort(array)

if __name__ == '__main__':
    unittest.main()
