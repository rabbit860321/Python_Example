a = 1
b = 3
score = 75
password = "Python2016"

if(a>=b):
    print("a>=b")
if(password == "python2016"):
    print("* 歡迎使用本系統")
if(score>60)and(score<=90):
    print("You are a outstanding student.")
#---------------
n = int(input("* 請輸入一個整數值:"))

if(n%2 == 0):
    print("%d 是偶數或零" %n)
else:
    print("%d 是奇數" %n)
#boolean--------
print("o"in"Hello")
print("h"in"Hello")
