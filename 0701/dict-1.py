# 字典 Dictionary

d1 = {}
d2 = {
    'name': 'John',
    'age': 25,
}

# print(d2)
# print(d2['age'])
# print(d2['mail'])

# print(d2.get('age'))
# print(d2.get('mail'))
d2['mail'] = 'asdf@gmail.com'
d2['age'] = 26
# del d2['mail']

# print(d2)
# for data in d2:
#     print(data)
#
# for data in d2.values():
#     print(data)
#
# for data in d2.keys():
#     print(data)
#
# for data in d2.items():
#     print(data)
#
# for k,v in d2.items():
#     print(k,v)

# update()
data = {
    'score': '95',
    'address': 'test',
    'name': 'John123'
}
d2.update(data)
print(d2)

print('John123' in d2.values())
print('age' in d2.keys())


print(len(d2))