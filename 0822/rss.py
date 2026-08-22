import streamlit as st
import requests
import bs4

st.title('RSS')

rss_web = {
    '證交所':'https://www.twse.com.tw/rwd/zh/news/feed?type=rss',
    '衛福部' :'https://www.mohw.gov.tw/rss-16-1.html',
    '檢查局': 'https://www.feb.gov.tw/RSS/feb/Messages?serno=201504010001&language=chinese'
}

result = st.selectbox('請選擇要檢視的RSS', rss_web.keys())
count = st.selectbox('筆數',[5,10,15,20])
# count = st.text_input('請輸入筆數')
if st.button('取得'):
    response = requests.get(rss_web[result], verify=False)
    soup = bs4.BeautifulSoup(response.text, 'xml')
    items = soup.find_all('item')
    for item in items[:int(count)]:
        title = item.find('title').text

        # st.markdown(f'- {item.pubDate.text} {title}')
        with st.container(border=True):
            st.write(title)
            st.write(item.pubDate.text)
