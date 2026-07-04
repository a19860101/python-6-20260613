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

print(len(s1) )

print(s1)