import streamlit as st
import pandas as pd

st.title("The Best Company")
col1 = st.columns(1)

content = 'Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit... '
content2 = '\" There is no one who loves pain itself, who seeks after it and wants to have it, simply because it is ' \
           'pain... \"'
content3 = content + content2
col1[0].write(content3)

st.subheader("Our Team")

df = pd.read_csv('data.csv', sep=',')


#if __name__ == '__main__':
