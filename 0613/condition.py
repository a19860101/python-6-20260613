# 條件式、判斷式

x = 10
# if

# if x == 10:
#     print(True)

# if x > 10:
#     print('success')
# else:
#     print('fail')

# if x > 10:
#     print('A+')
# elif x > 5:
#     print('A')
# else:
#     print('B')

# > >= < <= == !=

score = 100
# 注意順序，如果用大於，要由大比到小；反之用小於，就由小比到大
if score > 90:
    print('A+')
elif score > 80:
    print('A')
elif score > 70:
    print('B')
elif score > 60:
    print('C')
else:
    print('D')

day = 6
if day == 0:
    print('星期日')
elif day == 1:
    print('星期一')
elif day == 2:
    print('星期二')
elif day == 3:
    print('星期三')
elif day == 4:
    print('星期四')
elif day == 5:
    print('星期五')
elif day == 6:
    print('星期六')
