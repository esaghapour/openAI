import streamlit as st
import openai

# Set the API key for the openai library
tx=st.text_input("api_key:")
openai.api_key ='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'

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
st.write("The chatGPT model responded with:", response["choices"][0]["text"])
exec(response["choices"][0]["text"])
