import openai
import os
import gradio as gr
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

messages = [
    {"role": "system",
     "content": "You are a helpful AI assistant that can talk about everyday subjects."},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Talk to me")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="Your friendly AI Chatbot",
             description="We can talk about whatever you like",
             theme="compact").launch(share=True)

# Define the function to call the API
#def chat(prompt):
    # Set the API parameters
    #engine = "gpt-3.5-turbo" # this is a chat model
#    max_tokens = 60
#    temperature = 0.5 # the amount of randomness and creativity

    # Send the request to the API
#    response = openai.Completion.create(
#        engine="text-davinci-003",
#        prompt=prompt,
#        max_tokens=max_tokens,
#        temperature=temperature
#    )

    # Extract the response text
    #output = response.choices[0].text.strip()
    # Not sure if we want to strip or not yet
 #   output = response.choices[0].text

    # Print the response text
 #   print(output)

 #   return output

# Call the function with a prompt
#chat("Write a python function that calculates the area of a circle given its radius")

