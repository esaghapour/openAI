import streamlit as st
import openai

# Set the API key for the openai library
openai.api_key = "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"

# Get the text input from the user
text = st.text_input("Enter some text:")

# Use the chatGPT model to generate a response to the entered text
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=text,
    max_tokens=1024,
    n=1,
    temperature=0.5,
)

# Display the response in the app
st.write("The chatGPT model responded with:", response["choices"][0]["text"])
