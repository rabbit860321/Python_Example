import random

answer = random.randint(1,10) #1~10隨機整數
guest = 0
counter = 0


while True:
    guest = int(input("1~10猜一個數字->"))
    counter += 1
    if answer == guest:
        break
    else:
        print("錯了!")

print("猜對囉! 一共猜了:",counter,"次")
