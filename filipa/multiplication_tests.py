import unittest

from multiplication import mul


class MultiplicationTest(unittest.TestCase):
    
    def test_simple_mul(self):
        """
        Tests the one digit multiplication table
        """
        self.assertEquals(mul(5, 6), 30)

    def test_even_digits_mul(self):
        """
        Tests the simpler case where the number of digits is even
        """
        self.assertEquals(mul(49, 57), 2793)
        self.assertEquals(mul(5678, 1234), 7006652)

    def test_odd_digits_mul(self):
        """
        Tests the more complex case for odd digit numbers
        """
        pass

if __name__ == '__main__':
    unittest.main()
