import streamlit as st
import openai

st.title("My Chatbot")
st.write("Enter your OpenAI API key below:")
api_key = st.text_input("API Key", type="password")

if st.session_state.get("api_key") is None:
    st.session_state["api_key"] = api_key.strip()

if st.session_state["api_key"] != "":
    user_input = st.text_input("You:", "Type your message...")
    if user_input:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            temperature=0.5,
            max_tokens=100
        )
