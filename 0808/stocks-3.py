import yfinance
import mplfinance as mpl
import matplotlib.pyplot as plt

code = 'AAPL'
# result = yfinance.download(code, period='1mo', auto_adjust=False)
result = yfinance.download(code, start='2025-06-01' , end='2025-6-30', auto_adjust=False)
print(result.columns)
result.columns = result.columns.get_level_values(0)
print(result.columns)

market_color = mpl.make_marketcolors(
    up='red',
    down='green',
    inherit=True
)

style = mpl.make_mpf_style(
    marketcolors=market_color,
)


mpl.plot(result, type='candle', style=style)
