import streamlit as st
from google import genai
import streamlit as st
import google.generativeai as genai
import re

st.title("AI Tutor")

def get_openai_answer(text):
    api_key = st.secrets["MY_API_KEY"]
    genai.configure(api_key = api_key)

    safe = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE", # Increase threshold for harassment
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE", # Increase threshold for hate speech
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
    ]
    prompt = (
    "Create 10 multiple choice questions with four choices about the given topic. "
        "Format as:\n\n" +
        "1. **Question**\n" +
        "a) Option A\n" +
        "b) Option B\n" +
        "c) Option C\n" +
        "d) Option D\n\n" +
        "Make sure each option is on a new line. And the answer for each question is at the end after all questions" +
    "Create 10 multiple choice questions with four choices about the given topic below"
    )

    
    model = genai.GenerativeModel('gemini-1.5-pro')
    chat = model.start_chat(history=[])
    response = chat.send_message(prompt + text , safety_settings=safe)

    output = response.text
    return clean_format(output)

def clean_format(text):
    # Ensure answer choices start on new lines
    text = re.sub(r'\s*a\)', r'\n a)', text)
    text = re.sub(r'\s*b\)', r'\n b)', text)
    text = re.sub(r'\s*c\)', r'\n c)', text)
    text = re.sub(r'\s*d\)', r'\n d)', text)

    # Bold the questions (digits followed by period)
    text = re.sub(r'(\d+\.\s)(.*?)(?=\n| a\))', r'\1**\2**', text)

    return text

st.write("Question Creator")
text_input = st.text_input("Provide a topic")

if (st.button("Generate Questions")):
        answer = get_openai_answer(text_input)
        st.markdown(answer, unsafe_allow_html=True)


##AIzaSyAbnF3xUWoX8cvirqdZW6ot49gZVaLYlM0
