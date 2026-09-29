# Imports needed
import streamlit as st 
from ollama import chat 


# Set a title
st.title("AI Operations and Log Summeriser")

# Storing user input into a text box, into a callable vairable 
text = st.text_area(
    "Paste your text here:",
    height=200
)

# Creating a button, 'if' means the code is only run when clicked 
if st.button("Analyse with AI"):
    st.write(text)

