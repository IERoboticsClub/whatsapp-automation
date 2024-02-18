import streamlit as st
import datetime
from langchain_community.llms import Ollama

st.set_page_config(page_title="Whatsapp Automation", page_icon=":iphone:", layout="wide")

llm = Ollama(model="llama2:latest")

st.title('Whatsapp Automation')
st.text('<3')

form = st.form(key='my_form')
event = form.selectbox('Select an event', ('Workshop', 'POW'), index=None)
date = form.date_input('What day is the event?', value=None, format="DD/MM/YYYY")
time = form.time_input('What time is the event?', value=datetime.time(0, 0))
room = form.text_input('What is the room number?', value=None)
model = form.selectbox('Select a model', ('llama2:latest', 'gpt-3.5-turbo'), index=None)
# llm = Model(model)..

formatted_time = time.strftime('%H:%M')

# Adjusting the button to submit the form
if form.form_submit_button('Submit'):
    # Generating the prompt based on the event
    if event == 'Workshop':
        prompt = f'Please generate a message for a Workshop event in room {room}, at {formatted_time}, on {date}.'
    elif event == 'POW':
        prompt = f'Please generate a message for a Paper of the Week event in room {room}, at {formatted_time}, on {date}.'
    else:
        prompt = 'Please generate a generic message for an event.'

    # Using the llm to predict/generate the response based on the prompt
    response = llm.predict(prompt)

    # Displaying the generated message
    st.markdown(response)
