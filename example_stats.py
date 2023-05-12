import statistics

def calculate_stats(numbers):
    """
    Calculate the average, median, and standard deviation of a list of numbers.

    Parameters:
    numbers (list): A list of numbers.

    Returns:
    tuple: A tuple containing the average, median, and standard deviation.
    """
    # Calculate the average
    avg = sum(numbers) / len(numbers)

    # Calculate the median
    median = statistics.median(numbers)

    # Calculate the standard deviation
    stdev = statistics.stdev(numbers)

    return avg, median, stdev

numbers = [1, 2, 3, 4, 5]
avg, median, stdev = calculate_stats(numbers)
print(f"Average: {avg}")
print(f"Median: {median}")
print(f"Standard deviation: {stdev}")
