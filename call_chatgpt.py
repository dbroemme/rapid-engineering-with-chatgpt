import openai
import os

# Set the OpenAI key
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the function to call the API
# The temperature is the amount of randomness and creativity,
# a value between 0 and 2. Higher values make the output more random,
# while lower values are more focused and deterministic.
def generate_code(prompt, temperature = 0.5, max_tokens = 256):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature
    )

    # Extract the response text
    return response.choices[0].text.strip()

# Lets write some code
prompt = (
    "Write a python function that takes a String "
    "as input and returns a counts of the number "
    "of vowels in the string"
)
code = generate_code(prompt)
print(code)















