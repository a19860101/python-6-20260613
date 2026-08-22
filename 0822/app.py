import streamlit as st

home = st.Page('home.py', title='首頁')
rate = st.Page('rate.py',title='取得匯率')
rss = st.Page('rss.py',title='取得RSS')
weather = st.Page('weather.py', title='天氣資訊')

pg = st.navigation([home, rate, rss, weather])

pg.run()