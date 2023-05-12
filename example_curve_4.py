import gradio as gr
import matplotlib.pyplot as plt


def grading_curve(test_scores):
    max_score = max(test_scores)
    curved_scores = [(score / max_score) * 100 for score in test_scores]
    grades = []
    for score in curved_scores:
        if score >= 90:
            grades.append(('A', score))
        elif score >= 80:
            grades.append(('B', score))
        elif score >= 70:
            grades.append(('C', score))
        elif score >= 60:
            grades.append(('D', score))
        else:
            grades.append(('F', score))
    return grades

def str_list_to_num_list(str_list):
    num_list = []
    for string in str_list.split(","):
        try:
            num = float(string.strip())
            num_list.append(num)
        except ValueError:
            print(f"Could not convert {string} to a number.")
    return num_list

def display_grades(test_scores):
    test_scores = str_list_to_num_list(test_scores)
    print("The list of converted test scores is " + str(test_scores))
    grades = grading_curve(test_scores)

    # Create the table of grades
    table = f"{'Test Score':<12} {'Curved Score':<15} {'Letter Grade':<12}\n"
    for i, score in enumerate(test_scores):
        curved_score, letter_grade = grades[i][1], grades[i][0]
        table += f"{score:<12} {curved_score:<15.2f} {letter_grade:<12}\n"
    print(table)

    grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for grade in grades:
        grade_counts[grade[0]] += 1

    plt.bar(grade_counts.keys(), grade_counts.values())
    plt.xlabel("Letter Grade")
    plt.ylabel("Number of Students")
    plt.title("Distribution of Letter Grades")
    #plt.show()

    # Create the line graph of grades
    #plt.plot(test_scores, [grade[1] for grade in grades])
    #plt.title("Curved Test Scores")
    #plt.xlabel("Test Scores")
    #plt.ylabel("Curved Scores")

    return plt


# Define the Gradio interface
interface = gr.Interface(display_grades,
                         inputs=gr.inputs.Textbox(label="Enter a comma-separated list of test scores (0-100)"),
                         outputs=gr.Plot())

# Launch the web app
interface.launch()
