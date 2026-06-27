# 字串常用方法

s = 'hElLo wORLd'

print(s)
# 大寫
print(s.upper())
# 小寫
print(s.lower())
# 首字放大
print(s.capitalize())
# 單字首字放大
print(s.title())

# 取代 replace
s2 = 'hello world!!'
result = s2.replace('hello', '摳你機挖')
print(result)

# 尋找 find
# 尋找文字，找到的話回傳文字位置；找不到回傳-1
print(s2.find('o'))
print(s2.find('x'))
print(s2.find('hello'))
print(s2.find('world'))
print(s2.find('qqq'))