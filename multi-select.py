import streamlit as st
import openai
# Get the text input from the user
text ='write a sample code about scater plot in python using plotly package'

# Display the text in the app
st.write("You entered:", text)



# set the API key
openai.api_key = "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"


# specify the prompt to use

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=text,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
exec(response["choices"][0]["text"])
