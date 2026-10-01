# AI_Summariser
A beginner project, semi guided, instructions and rationale provided by ideation with AI

Having been thrown up quite quickly for simple functionality, I will begin to develop it further as I tinker with it and gain insight through activity. 

## Current Functionality

Takes text and runs it through the qwen3:8b local model (via Ollama) which will analyse the text under the instruction set of:

* Analyse the issue 
* Identify 'Key problem', 'Urgency level of the problem', 'Logical steps of Action (based upon what context it has)'
* Output response

## Structure

Written in Python. 

* Using Streamlit to create the body of the webpage and provide a UI to the user.
* Using Ollama to process the local model functionality.

### Roadmap (As best as I can see to make one)

Allowing user selection of the AI repsonse parameters is a current idea.

Buidling upon the scope of the Analyser, once a direction is found.

## Housekeeping

For the project repository itself a requirements.txt would be very handy to have.


