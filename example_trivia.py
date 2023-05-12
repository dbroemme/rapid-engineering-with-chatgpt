import openai
import os

from dotenv import load_dotenv
load_dotenv()
def generate_trivia_questions(topic):
    # Set up OpenAI API key
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Define the prompt to generate trivia questions on the given topic
    prompt = """Generate two trivia questions on the topic of U.S. Presidents.
    For each question, provide four possible answers labeled A, B, C, and D, and indicate which is the correct answer.
    Format your response as a JSON list.
    Each object in the JSON list should have the format:
    ```{ "Question": ..., "A": ..., "B": ..., "C": ..., "D": ..., "Answer":, ... }```
    """

    # Use ChatGPT to generate the questions and answers
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        temperature=0.7,
    )

    return response.choices[0].text



questions = generate_trivia_questions("U.S. Presidents")
print("-----")
print(questions)
print("-----")
