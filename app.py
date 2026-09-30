# Imports needed
import streamlit as st 
from ollama import chat 


# Set a title
st.title("AI Operations and Log Summeriser")

# Details in a caption
st.caption("Using Ollama to run a local model qwen3:8b")

# Storing user input into a text box, into a callable vairable 
user_input_text = st.text_area(
    "Paste your text here:",
    height=200
)

# Creating a button, 'if' means the code is only run when clicked 
if st.button("Analyse with AI"):
    st.write(user_input_text)

# Sending the input to Gemma & storing the response into a variable
model_response = chat(
    model="qwen3:8b",
   messages=[
    {
        "role": "user",
        "content": f"""
            Analyse the following operations or log text.

            Identify:
            1. The key problem
            2. The urgency level
            3. Recommended action

            Text:
            {user_input_text}
            """
        }
    ]
)

# 'Print' the response to the webpage
st.write(model_response.message.content)

