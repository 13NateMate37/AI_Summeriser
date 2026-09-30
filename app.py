# Imports needed
import streamlit as st 
from ollama import chat 


# Set a title
st.title("AI Issue Analyser")

# Details in a caption
st.caption("Using Ollama to run a local model qwen3:8b")

# Storing user input into a text box, into a callable vairable 
user_input_text = st.text_area(
    "Paste your text here:",
    height=200
)

# Header above the model response
st.subheader("Qwen's Output")

# Creating a button, 'if' means the code is only run when clicked 
if st.button("Analyse with AI"):
    if not user_input_text.strip():
        st.warning("Paste text for analysis first")
    else:
        with st.spinner("Analysing..."):
            # Sending the input to Qwen & storing the response into a variable
            model_response = chat(
                model="qwen3:8b",
            messages=[
                {
                    "role": "user",
                    "content": f"""
                        Analyse the following issue.

                        Identify:
                        1. The key problem
                        2. The urgency level
                        3. Recommended action

                        Text:
                        {user_input_text}
                        """
                    }
                ],
            )
        # 'Print' the response to the webpage
        st.write(model_response.message.content)


