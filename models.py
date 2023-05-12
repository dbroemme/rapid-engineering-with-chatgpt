from datetime import datetime

class Quiz:
    def __init__(self, id, name, created_at):
        self.id = id
        self.name = name
        self.created_at = created_at

class Question:
    def __init__(self, question_id, question_text, option_a, option_b, option_c, option_d, correct_answer, quiz_id):
        self.question_id = question_id
        self.question_text = question_text
        self.option_a = option_a
        self.option_b = option_b
        self.option_c = option_c
        self.option_d = option_d
        self.correct_answer = correct_answer
        self.quiz_id = quiz_id

class Result:
    def __init__(self, result_id, username, number_correct, total_questions, numeric_grade, creation_timestamp, quiz_id):
        self.result_id = result_id
        self.username = username
        self.number_correct = number_correct
        self.total_questions = total_questions
        self.numeric_grade = numeric_grade
        self.creation_timestamp = creation_timestamp
        self.quiz_id = quiz_id
