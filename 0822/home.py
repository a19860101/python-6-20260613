import streamlit as st

st.title('首頁')
st.write('hello world')

# st.markdown("""
# ## title
#
# - test
# - test
#
# """)

with open('0822/test.md', 'r', encoding='utf-8')as f:
    st.markdown(f.read())

st.title('hello')