import random
while True:
    print('猜數字遊戲開始')
    h = int(input('請輸入要猜的最大值：'))
    ans = random.randint(1,h)

    low=1
    high=h
    print(ans)
    while True:
        guess = input('請輸入數字：')
        guess = int(guess)
        if guess > ans:
            high = guess
            print(f'太大啦。{low}-{high}之間')
        elif guess < ans:
            low = guess
            print(f'太小啦。{low}-{high}之間')
        else:
            print('恭喜')
            break

    again = input('要再玩一場嗎？任意鍵繼續或輸入n結束：')
    if again.lower() == 'n':
        print('掰!下次見!!')
        break