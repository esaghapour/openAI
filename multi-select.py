import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI()

# Function to create completions using OpenAI API
def create_completion(api_key, model, messages):
    client.api_key = api_key
    completion = client.chat.completions.create(model=model, messages=messages)
    return completion.choices[0].message

# Streamlit app
def main():
    st.header('OpenAI ChatGPT Streamlit App')

    # Get API key from user input
    api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")

    # Example messages
    messages = [
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]

    # Generate completion when button is clicked
    if st.button("Generate Response"):
        # Ensure API key is provided
        if not api_key:
            st.error("Please enter your OpenAI API key.")
        else:
            try:
                # Generate completion using OpenAI API
                completion = create_completion(api_key, "gpt-3.5-turbo", messages)
                st.write("Response:")
                st.write(completion)
            except Exception as e:
                st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
