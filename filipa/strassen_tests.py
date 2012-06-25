# encoding:utf-8
import unittest

from strassen import multiply_matrices, seven_products


class MultiplyMatricesTest(unittest.TestCase):
    """
    Tests the matrices multiplication algorithms
    """
    def test_seven_products(self):
        values = 1, 2, 3, 4, 5, 6, 7, 8
        result = seven_products(*values)
        expected_result = -2, 24, 35, 8, 65, -30, -22
        self.assertEquals(len(result), 7)
        self.assertEquals(result, expected_result)

    def test_multiplication_basic(self):
        pass
        #m1 = [[1, 2], [3, 4]]
        #m2 = [[1, 2], [3, 4]]
        #m1m2 = [[7, 10], [11, 22]]
        #self.assertEquals(multiply_matrices(m1, m2), m1m2)

if __name__ == '__main__':
    unittest.main()
