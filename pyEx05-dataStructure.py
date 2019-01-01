#----List----
A = [1,2,3,4,5]
B = ["boy","girl","friend","sister","brother"]
y = [1,2,"hello"]  #List型態可以不必一樣

print('A[1]:',A[1])
print('B[3]:',B[3])
print('y[2]:',y[2])
print('A[2:4]:',A[2:4])

C = B[:]       #List複製
print(C)

print('B陣列長度:',len(B))  #len()可得到List的長度

del(A[2])      #del()可刪除List的元素
print(A)

for e in B:   #印出陣列B每一個元素
    print(e)
print('---------')
#----Tuple----
#Tuple資料內容不能改變
X = (1,2,3)
T = (1,2,3,4,5)

print('X[1]:',X[1])
list(T)      #list()可以將Tuple轉成List

a,b,c = X    #Tuple具有分解指定功能
print(a,b,c)
print('----------')
#----Dictionary----
#key必須唯一
dict = {'Name':'Zara','Age':7,'Class':'First'}

print("dict['Name']:",dict['Name'])
print("dict['Age']:",dict['Age'])

dict['Age'] = 8

print("dict['Age']:",dict['Age'])

del dict['Name']  #刪除Key是'Name'的條目
dict.clear        #清空字典所有條目
del dict          #刪除字典

