import sqlite3

def save_quiz_data(quiz):
    # Connect to database
    conn = sqlite3.connect('quizdb.sqlite')
    c = conn.cursor()

    # Insert quiz data into quiz table
    c.execute("INSERT INTO quiz (id, name, created_at) VALUES (?, ?, ?)",
              (quiz.id, quiz.name, quiz.created_at))

    # Commit changes to database and close connection
    conn.commit()
    conn.close()

def save_quiz_questions(questions):
    # Connect to the database
    conn = sqlite3.connect('quizdb.sqlite')
    c = conn.cursor()

    # Generate the SQL query
    sql = 'INSERT INTO questions (question_id, question_text, option_a, option_b, option_c, option_d, correct_answer, quiz_id ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'

    for question in questions:

        # Execute the query
        c.execute(sql,(question.question_id,
                       question.question_text,
                       question.option_a,
                       question.option_b,
                       question.option_c,
                       question.option_d,
                       question.correct_answer,
                       question.quiz_id))

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()

def save_quiz_result(result):
    # Connect to database
    conn = sqlite3.connect('quizdb.sqlite')
    c = conn.cursor()

    # Insert quiz data into quiz table
    c.execute("INSERT INTO results (result_id, username, number_correct, total_questions, numeric_grade, created_at, quiz_id) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (result.result_id, result.username, result.number_correct, result.total_questions, result.numeric_grade, result.created_at, result.quiz_id))

    # Commit changes to database and close connection
    conn.commit()
    conn.close()
