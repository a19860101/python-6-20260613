ntd = input('請輸入台幣金額：')
# print(type(ntd))
usd = float(ntd) / 32

# print('台幣'+ntd+'約為美金'+str(usd))
# f-string
print(f'台幣{ntd}約為美金{usd}')