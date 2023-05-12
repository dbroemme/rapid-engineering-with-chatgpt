import openai
import os
import gradio as gr
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

messages = [
    {"role": "system",
     "content": "You are an expert travel advisor. " +
                "Do not talk about anything other than travel. " +
                "Help people plan their perfect vacation."},
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

inputs = gr.inputs.Textbox(lines=7, label="Tell me about your travel plans")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Travel Advisor",
             description="Plan your perfect vacation",
             theme="compact").launch(share=True)