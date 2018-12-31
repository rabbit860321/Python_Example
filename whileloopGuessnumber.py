import random

answer = random.randint(1,100)
runing = True

while runing:
    guess = int(input('1~100猜一個數字:'))
    if guess == answer:
        print('恭喜 你猜中了!')
        runing = False
    elif guess < answer:
        print('太小了!')
    else:
        print('太大了!')
        
