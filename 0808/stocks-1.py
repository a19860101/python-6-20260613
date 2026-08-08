import yfinance
import matplotlib.pyplot as plt

# code = ['0050.TW','0056.TW']

# code = input('請輸入台股代碼：')

code = '0050.TW'

result = yfinance.download(code, period='1mo')
# result = yfinance.download(code, start='2026-01-01', end='2026-08-07')

# print(result)
plt.plot(result.index, result['High'])
plt.plot(result.index, result['Low'])
plt.plot(result.index, result['Close'])

plt.show()



