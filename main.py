import os
from dotenv import load_dotenv
import streamlit as st
from langchain.llms import OpenAI

# Load environment variables from .env file
load_dotenv()

# Access the API key from the environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

st.title('🦜🔗 Personal Assistant')

def generate_response(input_text):
  if openai_api_key:
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))
  else:
    st.warning('Please set the OPENAI_API_KEY environment variable in the .env file!', icon='⚠')

with st.form('my_form'):
  text = st.text_area('Enter text:')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key:
    st.warning('Please set the OPENAI_API_KEY environment variable in the .env file!', icon='⚠')
  if submitted:
    generate_response(text)
