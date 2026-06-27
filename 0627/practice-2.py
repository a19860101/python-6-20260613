import random

# q = ['apple', 'banana', 'mango', 'pineapple', 'kiwi']

# print(random.random())
# print(random.randint(1,99))
# print(random.randrange(1,10))
# print(random.choice(q))

ans = random.randint(1,10)
print('猜數字遊戲開始')
print(ans)

while True:
    guess = input('請輸入數字：')
    guess = int(guess)
    if guess > ans:
        print('太大')
    elif guess < ans:
        print('太小')
    else:
        print('恭喜')
        break
