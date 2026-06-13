# 簡單貨幣計算-

ntd = input('請輸入台幣金額：')
# print(type(ntd))
if not ntd.isdigit():
    exit('請輸入正確的數字')

usd = float(ntd) / 32

# print('台幣'+ntd+'約為美金'+str(usd))
# f-string
print(f'台幣{ntd}約為美金{usd}')
