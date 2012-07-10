# encoding:utf-8
import unittest

from karger import remove_self_loops


class KargerTest(unittest.TestCase):
    """
    Tests the karger algorithm
    """
    def test_remove_self_loops(self):
        graph = {'2': ['3', '4', '2']}
        expected_graph = {'2': ['3', '4']}
        remove_self_loops(graph, '2')
        self.assertEquals(graph, expected_graph)
        graph = {'2': ['3', '2', '4', '2']}
        remove_self_loops(graph, '2')
        self.assertEquals(graph, expected_graph)
        graph = {'2': ['3', '2', '4', '2', '2']}
        remove_self_loops(graph, '2')
        self.assertEquals(graph, expected_graph)
        

if __name__ == '__main__':
    unittest.main()
