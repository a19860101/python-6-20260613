while True:
    m = input('請選擇功能：1)台幣轉美金 2)台幣轉日幣 q)結束程式：')
    if m.lower() == 'q':
        print('BYE')
        break
    if m != '1' and m != '2':
        print('請輸入正確的功能')
        continue

    ntd = input('請輸入金額')
    if not ntd.isdigit():
        print('請輸入正確的數字')
        continue
    if m == '1':
        result = int(ntd) / 32
        print(f'台幣{int(ntd):,}約為美金{result:.0f}')
    elif m == '2':
        result = int(ntd) / 0.198
        print(f'台幣{int(ntd):,}約為日幣{result:,.0f}')