from models import Quiz
from save_quiz import save_quiz_data
from save_quiz import save_quiz_questions
import datetime
import uuid

from generate_questions import generate_questions
from generate_questions import parse_questions_json
from generate_questions import create_quiz

create_quiz("Science", 3)

#questions = generate_questions("Basketball", 3)
#questions = """[
#  {
#    "Question": "What team won the most World Series Titles?",
#    "A": "New York Yankees",
#    "B": "Boston Red Sox",
#    "C": "St. Louis Cardinals",
#    "D": "Los Angeles Dodgers",
#    "Answer": "A"
#  },
#  {
#    "Question": "What Hall of Famer was nicknamed 'The Say Hey Kid'?",
#    "A": "Mickey Mantle",
#    "B": "Willie Mays",
#    "C": "Hank Aaron",
#    "D": "Babe Ruth",
#    "Answer": "B"
#  },
#  {
#    "Question": "What team won the 2020 World Series?",
#    "A": "Los Angeles Dodgers",
#    "B": "San Francisco Giants",
#    "C": "Houston Astros",
#    "D": "New York Yankees",
#    "Answer": "A"
#  }
#]
#"""
#question_objects = parse_questions_json(questions, 3828988818793358004)
#save_quiz_questions(question_objects)
#quiz_id = uuid.uuid1().int
#current_time = datetime.datetime.now()
#quiz = Quiz(quiz_id, 'Secopnd Real Quiz', current_time)
#new_quiz_id = save_quiz_data(quiz)
#print("The new quiz id is is " + str(new_quiz_id))

#quizzes = get_quiz_list()
#for quiz in quizzes:
#    print(vars(quiz))
