import streamlit as st
import requests


st.title("My Chatbot")
st.write("Enter your Open API key below:")
api_key = st.text_input("API Key", type="password")


def get_response(query, api_key):
    url = "https://api.openai.com/v1/engines/davinci-codex/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    payload = {
        "prompt": query,
        "max_tokens": 50,
        "n": 1,
        "stop": None,
        "temperature": 0.5,
    }
    response = requests.post(url, headers=headers, json=payload)
