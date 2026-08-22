import streamlit as st

home = st.Page('home.py', title='首頁')
rate = st.Page('rate.py',title='取得匯率')
rss = st.Page('rss.py',title='取得RSS')

pg = st.navigation([home, rate, rss])

pg.run()