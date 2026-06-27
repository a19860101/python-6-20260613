# 串列方法

fruits = ['apple','pineapple','kiwi','banana','Mango','Coconut']
print(fruits)
# append() 新增項目
# fruits.append('orange')

# insert() 在指定位置新增項目
# fruits.insert(0,'orange')

# extend() 新增可迭代物件
# 可迭代物件
# fruits.extend(['orange', 'kiwi','orange'])
# print(fruits)

# remove() 移除項目
# fruits.remove('orange')

# fruits.pop(0)

# del 透過索引移除項目
# del fruits[-1]
# print(fruits)
# clear() 清空串列
# fruits.clear()

# 修改串列
# fruits[2] = '芒果'

# 查詢

# index()
# 判斷資料位置，如果存在回傳索引；如果不存在則會報錯
# q = fruits.index('melon')

# count()
# 計算資料數量，回傳資料個數，不存在回傳0
# q2 = fruits.count('melon')
# print(q2)

# 判斷資料是否存在，回傳布林值
# print('orange' in fruits)
# print('melon' in fruits)

# 排序
# fruits.sort(key=str.lower)
# fruits.sort(reverse=True)

# fruits.reverse()
print(fruits)
