import sqlite3
from models import Quiz
from models import Question
from models import Result

def get_quiz_list():
    conn = sqlite3.connect('quizdb.sqlite')
    c = conn.cursor()
    c.execute("SELECT id, name, created_at FROM quiz")
    rows = c.fetchall()
    quiz_data = []
    for row in rows:
        quiz = Quiz(*row)
        quiz_data.append(quiz)
    conn.close()
    return quiz_data

def get_questions(quiz_id):
    # Connect to the database
    conn = sqlite3.connect('quiz_questions.sqlite')
    c = conn.cursor()

    c.execute("SELECT question_id, question_text, option_a, option_b, option_c, option_d, correct_answer, quiz_id FROM questions where quiz_id = " + str(quiz_id))
    rows = c.fetchall()
    questions = []
    for row in rows:
        quiz = Question(*row)
        questions.append(quiz)
    conn.close()
    return questions

