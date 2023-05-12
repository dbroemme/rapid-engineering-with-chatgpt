import statistics

class SummaryStatistics:
    def __init__(self, lst):
        # Validate the lst
        if not lst or len(lst) < 2:
            raise ValueError('lst should contain at least two numbers')
        if any([not isinstance(x, int) and not isinstance(x, float) for x in lst]):
            raise TypeError('lst should contain only numbers')

        self.average = sum(lst) / len(lst)
        self.median = statistics.median(lst)
        self.stdev = statistics.pstdev(lst)

# example usage:
#lst = [1, 2, 3, 4, 5]
#stats = SummaryStatistics(lst)
#print(stats.average)  # output: 3.0
#print(stats.median)  # output: 3
#print(stats.stdev)  # output: 1.5811388300841898
