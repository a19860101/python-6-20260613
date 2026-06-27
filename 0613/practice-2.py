m = input('請選擇功能1)台幣轉美金 2)台幣轉日幣：')
if m != '1' and m != '2':
    exit('請輸入正確的功能')

ntd = input('請輸入金額')
if not ntd.isdigit():
    exit('請輸入正確的數字')

if m == '1':
    result = int(ntd) / 32
    print(f'台幣{int(ntd):,}約為美金{result:.0f}')
elif m == '2':
    result = int(ntd) / 0.198
    print(f'台幣{int(ntd):,}約為日幣{result:,.0f}')