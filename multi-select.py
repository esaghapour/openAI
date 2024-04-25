import streamlit as st
import requests

# Function to make API requests
def fetch_data(query, api_key):
    url = "API_ENDPOINT_HERE"
    headers = {"Authorization": f"Bearer {api_key}"}
    params = {"query": query}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return data

# Streamlit UI
def main():
    st.title("OpenAPI Chatbot")
    api_key = st.text_input("Enter your API key:")
    query = st.text_input("Enter your query:")
    if st.button("Submit"):
        if api_key:
            if query:
                try:
                    response = fetch_data(query, api_key)
                    st.write("Bot:", response['answer'])
                except Exception as e:
                    st.write("An error occurred:", e)
            else:
                st.write("Please enter a query.")
        else:
            st.write("Please enter your API key.")

if __name__ == "__main__":
    main()
