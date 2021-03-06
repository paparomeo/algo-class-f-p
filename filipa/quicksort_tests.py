# encoding:utf-8
import unittest

from quicksort import quicksort, partition


class QuickSortTest(unittest.TestCase):
    """
    Tests the quicksort algorithm
    """
    def test_partition_1(self):
        array = [3, 5, 1, 4, 2, 6]
        self.assertEquals(partition(array, 0, 5), (0, 4, 6, 5))

    def test_partition_2(self):
        array = [3, 8, 2, 5, 1, 4, 7, 6]
        self.assertEquals(partition(array, 0, 7), (0, 4, 6, 7))

    def test_sort_basic(self):
        array = [1]
        ordered = [1]
        self.assertEquals(quicksort(array), ordered)
        
    def test_sort_basic_2(self):
        array = [3, 1]
        self.assertEquals(quicksort(array), sorted(array))
        
    def test_sort_4(self):
        array = [3, 1, 2, 4]
        self.assertEquals(quicksort(array), sorted(array))

    def test_sort_lesson_example(self):
        array = [1, 3, 5, 2, 4, 6]
        self.assertEquals(quicksort(array), sorted(array))

    def test_sort_max(self):
        array = [6, 5, 4, 3, 2, 1]
        self.assertEquals(quicksort(array), sorted(array))

    def test_exercise(self):
        with open('QuickSort.txt') as f:
            array = [int(line.strip()) for line in f.readlines()]
            self.assertEquals(quicksort(array), sorted(array))

if __name__ == '__main__':
    unittest.main()

