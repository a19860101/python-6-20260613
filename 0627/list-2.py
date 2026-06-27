# 串列方法

fruits = ['apple','banana','mango']
print(fruits)
# append() 新增項目
# fruits.append('orange')

# insert() 在指定位置新增項目
# fruits.insert(0,'orange')

# extend() 新增可迭代物件
# 可迭代物件
fruits.extend(['orange', 'kiwi','orange'])
print(fruits)

# remove() 移除項目
fruits.remove('orange')

# del 透過索引移除項目
# del fruits[-1]

# clear() 清空串列
# fruits.clear()

# 修改串列
fruits[2] = '芒果'

print(fruits)
