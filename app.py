import streamlit as st
from openai import OpenAI

def get_openai_answer(text):
    api_key = st.secrets["MY_API_KEY"]
    client = OpenAI(api_key = api_key)
       
    prompt = f" Create 10 multiple choice questions with four choices about {text} make sure these aren't just clarifying questions but rather questions that are meaningful"

    response = client.responses.create(
        model="gpt-5",
        reasoning={"effort": "medium"},
        input=[
            {
                 "role": "user", 
                 "content": prompt
            }
        ]
    )
       
    answer = response.output_text
    return answer

st.write("AI Question Creator")
text_input = st.text_input("Provide a topic")
if (st.button("Generate Questions")):
        answer = get_openai_answer(text_input)
        st.write(answer)