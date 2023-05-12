import unittest
import statistics
from example_stats_2 import SummaryStatistics

class SummaryStatisticsTest(unittest.TestCase):
    def setUp(self):
        self.lst = [1, 2, 3, 4, 5]
        self.stats = SummaryStatistics(self.lst)

    def test_average(self):
        self.assertEqual(self.stats.average, 3)

    def test_median(self):
        self.assertEqual(self.stats.median, 3)

    def test_stdev(self):
        self.assertEqual(self.stats.stdev, 1.5811388300841898)


if __name__ == '__main__':
    unittest.main()
