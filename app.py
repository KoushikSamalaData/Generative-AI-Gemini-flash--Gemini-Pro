import streamlit as st
import os
import pathlib
import textwrap

from IPython.display import display
from IPython.display import Markdown
#from altair.vegalite.v4.api import Chart

def to_markdown(text):
  text = text.replace('.',' *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

import os
os.environ['GEMINI_API_KEY']= 'AIzaSyB1KOZcG8QIC7MewHnpAh1VKJmzPrqwYY8'

import google.generativeai as genai
genai.configure(api_key=os.environ['GEMINI_API_KEY'])

## Function to load gemini model and get response

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(question)
    return response.text

## initialize our streamlit app

st.set_page_config(page_title="BOT Demo")

st.header("Gemini AI BOT Application")

input=st.text_input("Input: ",key="input")

submit=st.button("click me to generate response")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)
    
  