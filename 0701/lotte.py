import random

# 1
# result = []
# while True:
#     ans = random.randint(1, 49)
#     if ans in result:
#         continue
#     result.append(ans)
#     if len(result) == 6:
#         break
#
# print(result)

# 2

# result = random.sample(range(1,49), k=6)
# print(result)

# 3
cards = ['普通','稀有','超稀有']
weights = [80,15,5]
q = random.choices(cards, k=10, weights=weights)
print(q)