import streamlit as st
import openai

st.header('How to use ChatGPT and Streamlit')
# Set the API key for the openai library
api_key=st.sidebar.text_input("api_key:")
openai.api_key =api_key

# Get the text input from the user
text = st.text_input("Enter some text:")

# Use the chatGPT model to generate a response to the entered text
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=text,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

# Display the response in the app
st.code(response["choices"][0]["text"], language='python')
exec(response["choices"][0]["text"])
