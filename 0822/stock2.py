import streamlit as st
import yfinance
import mplfinance as mpl

st.title('K線圖')

code = st.text_input('請輸入股票代碼')
day = st.selectbox(
    '請輸入天數',
    ['15d','30d','60d','90d', '180d']
)
mean = st.selectbox(
    '請選擇均線',
    [5,10,15]
)
if st.button('取得'):
    data = yfinance.download(f'{code}', period=f'{day}')
    data.columns = data.columns.get_level_values(0)
    market_color = mpl.make_marketcolors(
        up='red',
        down='green',
        inherit=True
    )
    style = mpl.make_mpf_style(
        marketcolors=market_color,
    )
    mpl.plot(data, type='candle', style=style, volume=True, mav=mean, savefig='kline.png')
    st.image('kline.png')