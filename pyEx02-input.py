import sys
data = input("* 請輸入一個數字:")

print(data)
print(type(data)) #input()輸入的內容皆以String來處理
#---------
a = int(input(" *請輸入第一個數字:"))
b = int(input(" *請輸入第二個數字:"))
print(a,b)
print(type(a),type(b))
print(a+b)
#---------
x = sys.stdin.read(5)  #讀取5個字元,若不足則繼續等待
print(x)


