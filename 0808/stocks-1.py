import yfinance

# code = ['0050.TW','0056.TW']

code = input('請輸入台股代碼：')

result = yfinance.download(f'{code}.TW', period='1mo')

print(result)