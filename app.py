import streamlit as st
import datetime

st.title('Whatsapp Automation')
st.text('<3')

form = st.form(key='my_form')
event = form.selectbox('Select an event', ('Workshop', 'POW'), index=None)
datetime = form.date_input('What day the event?',value=None,format="DD/MM/YYYY")
time = form.time_input('What time is the event?',value=None)
st.write(f'There is a {event}, at {time}, on {datetime}')

form.form_submit_button('Submit')
