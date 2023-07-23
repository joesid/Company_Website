import streamlit as st
from send_email import send_email
import pandas as pd

st.header("Contact Me")

df = pd.read_csv('topics.csv', sep=',')
topic = df['topic'].tolist() #read content of column 'topic'

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    selected_option = st.selectbox("What topic do you want to discuss:", topic)
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New email from {user_email}

Topic: {selected_option}
From: {user_email}

{raw_message}
"""
    button = st.form_submit_button('Submit')
    if button:
        send_email(message)
        st.info("Your email was sent successfully")

