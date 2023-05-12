import unittest
import statistics
import random
from example_stats_2 import SummaryStatistics

class SummaryStatisticsTest(unittest.TestCase):
    # Test with random list of elements
    def test_random_list(self):
        lst = [random.randint(1, 100) for i in range(10)]
        stats = SummaryStatistics(lst)
        self.assertEqual(stats.average, statistics.mean(lst))
        self.assertEqual(stats.median, statistics.median(lst))
        self.assertAlmostEqual(stats.stdev, statistics.stdev(lst), places=6)

if __name__ == '__main__':
    unittest.main()
