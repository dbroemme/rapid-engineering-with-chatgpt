def grading_curve(test_scores):
    # Calculate the maximum score in the list
    max_score = max(test_scores)

    # Calculate the scaled grade and letter grade for each student
    grades = []
    for score in test_scores:
        scaled_grade = score * 100 / max_score
        if scaled_grade >= 90:
            letter_grade = 'A'
        elif scaled_grade >= 80:
            letter_grade = 'B'
        elif scaled_grade >= 70:
            letter_grade = 'C'
        elif scaled_grade >= 60:
            letter_grade = 'D'
        else:
            letter_grade = 'F'
        grades.append((scaled_grade, letter_grade))

    # Define the score range for each letter grade
    grade_ranges = {'A': (90, 100),
                    'B': (80, 89),
                    'C': (70, 79),
                    'D': (60, 69),
                    'F': (0, 59)}

    # Calculate the number of students in each letter grade range
    grade_counts = {grade: len([sg for sg, lg in grades if rg[0] <= sg <= rg[1]]) for grade, rg in grade_ranges.items()}

    # Calculate the percentage of students in each letter grade range
    total_students = len(grades)
    grade_percentages = {grade: count * 100 / total_students for grade, count in grade_counts.items()}

    # Return the grades, grade ranges, and percentages as a dictionary
    return {'Grades': grades, 'Grade Percentages': grade_percentages}


def display_grades(test_scores, grades):
    if not grades:
        print("No grades available")
        return

    if len(grades["Grades"]) != len(test_scores):
        print("Number of grades does not match number of test scores")
        return

    # Print the header row of the table
    print(f"{'Test Score':<12} {'Curved Score':<15} {'Letter Grade':<12}")

    # Print each row of the table
    for i, score in enumerate(test_scores):
        curved_score, letter_grade = grades["Grades"][i][0], grades["Grades"][i][1]
        print(f"{score:<12} {curved_score:<15.2f} {letter_grade:<12}")


test_scores = [75, 88, 92, 60, 81, 70, 85, 76, 90, 67]
grade_data = grading_curve(test_scores)

display_grades(test_scores, grade_data)
