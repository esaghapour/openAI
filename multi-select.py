

import openai
import streamlit as st

def generate_response(prompt, api_key, temperature=0.7, max_tokens=150):
    openai.api_key = api_key
    response = openai.Completion.create(  # Replace with the appropriate method from 1.0.0 API
        engine="text-davinci-003",  # Adjust engine as needed
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
    )
    return response.choices[0].text.strip()

st.title("Streamlit Chatbot with OpenAI")

# Input for API key
api_key = st.text_input("Enter your OpenAI API Key", type="password")

if api_key:
    # Input field for user text
    user_input = st.text_input("You: ")

    if user_input:
        # Generate response using provided API key
        response = generate_response(prompt=user_input, api_key=api_key)
        st.text(f"Chatbot: {response}")
else:
    st.warning("Please enter your OpenAI API key to proceed.")
