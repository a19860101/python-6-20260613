import yfinance
import mplfinance as mpl
import matplotlib.pyplot as plt

code = '0050.TW'
result = yfinance.download(code, period='3mo')
print(result.columns)
result.columns = result.columns.get_level_values(0)
print(result.columns)
mpl.plot(result, type='candle')