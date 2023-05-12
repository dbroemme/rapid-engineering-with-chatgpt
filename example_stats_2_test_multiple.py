import unittest
import statistics
from example_stats_2 import SummaryStatistics

class SummaryStatisticsTest(unittest.TestCase):
    # Test with empty list
    def test_empty_list(self):
        lst = []
        self.assertRaises(ValueError, SummaryStatistics, lst)

    # Test with one element
    def test_one_element_list(self):
        lst = [1]
        self.assertRaises(ValueError, SummaryStatistics, lst)

    # Test with two element
    def test_two_element_list(self):
        lst = [1, 3]
        stats = SummaryStatistics(lst)
        self.assertEqual(stats.average, 2)
        self.assertEqual(stats.median, 2)
        self.assertEqual(stats.stdev, 1)

if __name__ == '__main__':
    unittest.main()
