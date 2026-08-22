import streamlit as st
# st.markdown("""
# ## title
#
# - test
# - test
#
# """)
# st.subheader('版本控制')
with open('0822/版本控制.md', 'r', encoding='utf-8')as f:
    st.markdown(f.read())
