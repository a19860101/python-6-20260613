# 元組 tuple

t = ('apple','banana','orange')
# t = 'apple','banana','orange'
# t = ('apple',)
t2 = ('kiwi',)
# t = ()
# t = tuple()
print(type(t))
t3 = t + t2

print(len(t3))
print(t3.count('apple'))
print(t3.index('apple'))

print(t3[0])
print(t3[-1])
print(t3[1:3])
print(t3[::2])
print(t3[::-1])

coord = (23.5, 121.2)
lat, lon = coord

print(lat, lon)

