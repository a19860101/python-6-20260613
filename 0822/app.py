import streamlit as st

home = st.Page('home.py', title='首頁')
rate = st.Page('rate.py',title='取得匯率')
rss = st.Page('rss.py',title='取得RSS')
weather = st.Page('weather.py', title='天氣資訊')
stock = st.Page('stock.py', title='股價查詢')
stock2 = st.Page('stock2.py', title='K線圖')
pg = st.navigation([home, rate, rss, weather,stock, stock2])

pg.run()