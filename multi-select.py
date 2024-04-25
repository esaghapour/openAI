import streamlit as st
import openai

def ask_openai(question, api_key):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": question}]
    )
    return response['choices'][0]['message']['content']

st.title('OpenAI Chatbot')

# User inputs their API key
api_key = st.text_input("Enter your OpenAI API key:", type="password")

if api_key:
    user_question = st.text_input("Ask me anything:")
    if user_question:
        response = ask_openai(user_question, api_key)
        st.write(f"AI: {response}")
else:
    st.warning("Please enter your API key to proceed.")
