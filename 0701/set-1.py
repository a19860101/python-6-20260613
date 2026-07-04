# 集合 set
# 不可重複
# 無序

s1 = {1,2,2,2,2,2,2,3,4,5}
s2 = set()

s1.add(10)
# s1.remove(66)
s1.discard(66)
s1.update({123})
s1.update({5})

# print(len(s1) )

# print(s1)

q1 = {'A','B','C','F'}
q2 = {'A','B','E','F'}

# 交集
print(q1 & q2)
print(q1.intersection(q2))
# 聯集
print(q1 | q2)
print(q1.union(q2))
# 差集
print(q1 - q2)
print(q2 - q1)
print(q1.difference(q2))
print(q2.difference(q1))

# 對稱差集
print(q1 ^ q2)
print(q1.symmetric_difference(q2))