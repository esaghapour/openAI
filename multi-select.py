import streamlit as st
import openai
# Get the text input from the user
text = st.text_input("Enter some text:")

# Display the text in the app
st.write("You entered:", text)



# set the API key
openai.api_key = "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"

# specify the model to use (in this case, the "text-davinci-002" model)
model = "code-davinci-002"

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
