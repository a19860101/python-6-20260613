import streamlit as st

st.title('Hello World!!! 123')
st.header('Header')
st.subheader('Subheader')
st.write('normal text')

name = st.text_input('請輸入姓名：')
currency = st.selectbox(
    '選項',
    ['USD','JPY','EUR']
)
if st.button('輸入'):
    st.write(name)
    st.write(currency)