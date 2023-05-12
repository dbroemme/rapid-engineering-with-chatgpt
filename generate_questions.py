import openai
import os
import json
import uuid
import datetime
from models import Quiz
from models import Question
from save_quiz import save_quiz_data
from save_quiz import save_quiz_questions
from dotenv import load_dotenv
load_dotenv()

def generate_questions(topic, number_of_questions):
    # Set up OpenAI API key
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Define the prompt to generate trivia questions on the given topic
    prompt = (
        "Generate " + str(number_of_questions) + " trivia questions on the topic of " + topic + "."
        "For each question, provide four possible answers labeled A, B, C, and D, and indicate which is the correct answer."
        "Format your response as a JSON list."
        "Each object in the JSON list should have the format:"
        "```{ \"Question\": ..., \"A\": ..., \"B\": ..., \"C\": ..., \"D\": ..., \"Answer\":, ... }"
    )

    # Use ChatGPT to generate the questions and answers
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        temperature=0.7,
    )

    # ChatGPT sometimes wraps the json in backticks, which are not valid json
    # So we need to remove those. We also remove and leading whitespace.
    return response.choices[0].text.replace("`", "").strip()


def parse_questions_json(data, quiz_id):
    # Parse the data
    questions_data = json.loads(data)

    # Create a list to store the Question objects
    questions = []

    # Iterate through the data and instantiate Question objects
    for question_data in questions_data:
        text = question_data['Question']
        choices = {
            'A': question_data['A'],
            'B': question_data['B'],
            'C': question_data['C'],
            'D': question_data['D'],
        }
        answer = question_data['Answer']

        question_id = uuid.uuid4().hex
        question = Question(question_id,
                            text,
                            choices['A'],
                            choices['B'],
                            choices['C'],
                            choices['D'],
                            answer,
                            quiz_id)
        questions.append(question)

    # Return the list of questions
    return questions

def create_quiz(topic, number_of_questions):
    # Construct the quiz
    quiz_id = uuid.uuid4().hex
    quiz = Quiz(quiz_id, topic, datetime.datetime.now())

    # Generate the questions
    questions = generate_questions(topic, number_of_questions)
    question_objects = parse_questions_json(questions, quiz_id)

    # Persist the quiz and its questions to the database
    quiz.save()
    for question in question_objects:
        question.save()
    print("Saved the quiz and " + str(len(question_objects)) + "questions to database")
