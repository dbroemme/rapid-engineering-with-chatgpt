import statistics

def calculate_grading_curve(scores):
    """
    Calculate the grading curve for a list of test scores.

    Parameters:
    scores (list): A list of test scores.

    Returns:
    dict: A dictionary containing the score ranges for each letter grade.
    """
    # Calculate the average score
    avg_score = sum(scores) / len(scores)

    # Define the score ranges for each letter grade
    a_range = (avg_score + 1.5 * statistics.stdev(scores), float('inf'))
    b_range = (avg_score + 0.5 * statistics.stdev(scores), avg_score + 1.5 * statistics.stdev(scores))
    c_range = (avg_score - 0.5 * statistics.stdev(scores), avg_score + 0.5 * statistics.stdev(scores))
    d_range = (avg_score - 1.5 * statistics.stdev(scores), avg_score - 0.5 * statistics.stdev(scores))
    f_range = (float('-inf'), avg_score - 1.5 * statistics.stdev(scores))

    # Create a dictionary with the score ranges for each letter grade
    grade_ranges = {
        "A": a_range,
        "B": b_range,
        "C": c_range,
        "D": d_range,
        "F": f_range
    }

    return grade_ranges

scores = [70, 85, 90, 92, 95, 98, 100]
grade_ranges = calculate_grading_curve(scores)
print(grade_ranges)
