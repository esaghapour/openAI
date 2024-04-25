import openai
import streamlit as st

def generate_response(prompt, api_key, temperature=0.7, max_tokens=150):
    """Generates a response using the OpenAI API.

    Args:
        prompt (str): The user's input to be used as a prompt.
        api_key (str): The OpenAI API key.
        temperature (float, optional): Controls the randomness of the generated text. Defaults to 0.7.
        max_tokens (int, optional): The maximum number of tokens to generate. Defaults to 150.

    Returns:
        str: The generated response from the OpenAI API.

    Raises:
        openai.error.InvalidRequestError: If an invalid request is made to the OpenAI API.
    """

    openai.api_key = api_key

    try:
        response = openai.Completion.create(  # Replace based on 1.0.0 API migration
            engine="text-davinci-003",  # Adjust engine as needed
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
        )
        return response.choices[0].text.strip()
    except openai.error.InvalidRequestError as e:
        # Handle potential API errors with a user-friendly message
        return f"An error occurred: {e}. Please check your API key or prompt format."

st.title("Streamlit Chatbot with OpenAI")

# Input for API key
api_key = st.text_input("Enter your OpenAI API Key", type="password")

if api_key:
    # Input field for user text
    user_input = st.text_input("You: ")

    if user_input:
        # Generate response using provided API key
        try:
            response = generate_response(prompt=user_input, api_key=api_key)
            st.text(f"Chatbot: {response}")
        except Exception as e:  # Catch any unexpected errors
            st.error(f"An unexpected error occurred: {e}")
else:
    st.warning("Please enter your OpenAI API key to proceed.")
