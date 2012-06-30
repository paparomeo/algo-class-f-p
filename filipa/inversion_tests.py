# encoding:utf-8
import unittest

from inversion import mergesort


class InversionTest(unittest.TestCase):
    """
    Tests the inversion count algorithm
    """
    def test_inversions_basic(self):
        array = [1]
        ordered = [1]
        inversions = 0
        self.assertEquals(mergesort(array), (ordered, inversions))
        
    def test_inversions_basic_2(self):
        array = [3, 1]
        ordered = [1, 3]
        inversions = 1
        self.assertEquals(mergesort(array), (ordered, inversions))
        
    def test_inversions_simple(self):
        array = [3, 1, 2, 4]
        ordered = [1, 2, 3, 4]
        inversions = 2
        self.assertEquals(mergesort(array), (ordered, inversions))

    def test_inversions_lesson_example(self):
        array = [1, 3, 5, 2, 4, 6]
        ordered = [1, 2, 3, 4, 5, 6]
        inversions = 3
        self.assertEquals(mergesort(array), (ordered, inversions))

    def test_max_inversions(self):
        array = [6, 5, 4, 3, 2, 1]
        ordered = [1, 2, 3, 4, 5, 6]
        inversions = 15
        self.assertEquals(mergesort(array), (ordered, inversions))

    def test_exercise(self):
        with open('IntegerArray.txt') as f:
            array = [int(line.strip()) for line in f.readlines()]
            print mergesort(array)[1]

if __name__ == '__main__':
    unittest.main()
