day = 6

match day:
    case 0:
        print('星期日')
    case 1:
        print('星期一')
    case 2:
        print('星期二')
    case 3:
        print('星期三')
    case 4:
        print('星期四')
    case 5:
        print('星期五')
    case 6:
        print('星期六')
    case _:
        print('錯誤')

x ='123a'
print(x.isdigit() is False)