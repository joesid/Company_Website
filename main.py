import streamlit as st
import pandas as pd

st.title("The Best Company")
col = st.columns(1)

content = 'Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit... '
content2 = '\" There is no one who loves pain itself, who seeks after it and wants to have it, simply because it is ' \
           'pain... \"'
content3 = content + content2
col[0].write(content3)

st.subheader("Our Team")

df = pd.read_csv('data.csv', sep=',')

col1, col2, col3 = st.columns(3)

#1st Column
with col1:
    for index, row in df[:4].iterrows():
        fname = (row["first name"])
        lname = (row["last name"])
        name = fname + ' ' + lname
        st.subheader(name)
        st.write(row["role"])
        image_file = (row["image"])
        st.image(f'./images/{image_file}')

#2nd Column
with col2:
    for index, row in df[4:8].iterrows():
        fname = (row["first name"])
        lname = (row["last name"])
        name = fname + ' ' + lname
        st.subheader(name)
        st.write(row["role"])
        image_file = (row["image"])
        st.image(f'./images/{image_file}')

#3rd Column
with col3:
    for index, row in df[8:13].iterrows():
        fname = (row["first name"])
        lname = (row["last name"])
        name = fname + ' ' + lname
        st.subheader(name)
        image_file = (row["image"])
        st.write(row["role"])
        st.image(f'./images/{image_file}')

#if __name__ == '__main__':
