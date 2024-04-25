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
def main():
    if st.session_state.get("api_key") is None:
        st.session_state["api_key"] = api_key.strip()

    if st.session_state["api_key"] != "":
        user_input = st.text_input("You:", "Type your message...")
        if user_input:
            response = get_response(user_input, st.session_state["api_key"])
            bot_response = response.choices[0].text.strip()
            st.markdown(f"Bot: {bot_response}")
