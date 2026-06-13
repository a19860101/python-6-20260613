# 迴圈
# for
# range(10) -> 0-9
# range(15) -> 0-14
# range(x) -> 0-(x-1)
# range(1,10) -> 1-9
# range(x,y) -> x - y-1

# for n in range(10):
#     print(n)
i = 15
# for n in range(i):
#     print('*' * (n+1))
# for n in range(i):
#     print('*' * (i-n))

for n in range(i):
    print(' ' * (i-n-1) + '*' * (2 * n + 1))