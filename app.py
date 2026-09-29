import streamlit as st 

st.title("AI Operations and Log Summeriser")

text = st.text_area(
    "Paste your text here:",
    height=200
)

if st.button("Analyse with AI"):
    st.write(text)

