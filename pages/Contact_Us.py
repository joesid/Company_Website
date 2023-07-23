import streamlit as st
#Call Send Email Function


st.header("Contact Me")

options = ["Option 1", "Option 2"]

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    selected_option = st.selectbox("What topic do you want to discuss:", options)
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button('Submit')
    if button:
        #Read From Send Email Function
        st.info("Your email was sent successfully")

