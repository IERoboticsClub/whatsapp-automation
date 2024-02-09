import streamlit as st
import datetime

st.title('Whatsapp Automation')
st.text('<3')

form = st.form(key='my_form')
event = form.selectbox('Select an event', ('Workshop', 'POW'), index=None)
date = form.date_input('What day the event?',value=None,format="DD/MM/YYYY")
time = form.time_input('What time is the event?',value=datetime.time(0,0))
room = form.text_input('What is the room number?',value=None)

formatted_time = time.strftime('%H:%M')

if event == 'Workshop':
    st.write(f'There is a {event}, in room {room}, at {formatted_time}, on {date}, hope to see you there!')
elif event == 'POW':
    st.write(f'There is a {event}, in room {room}, at {formatted_time}, on {date}, please read the paper!')

form.form_submit_button('Submit')
