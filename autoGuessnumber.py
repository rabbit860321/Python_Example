import random

answer = random.randint(1,10) #取得1~10中隨機整數

guest = 0
count = 0

print("要猜的數字是:",answer);

guest = random.randint(1,10) 
count +=1

while answer != guest:
    print(guest,"? 錯了!")
    guest = random.randint(1,10)
    count +=1

print( guest,"? 猜對了! 猜了",count,"次")
