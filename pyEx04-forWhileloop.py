for i in range(5):
    print(i)
else:
    print('The for loop is over')
#--------------
for letter in 'Python':
    print('* Current Letter:',letter)

fruits = ['banana','apple','mango']
for fruit in fruits:
    print('Current Letter:',fruit)

for index in range(len(fruits)):      #len()傳回列表元素個數
    print('Current Letter:',fruits[index])
#--------------
count = 1

while (count <=10):
    print('The count is:',count)
    count = count +1
#----break Continue--
while True:
    s = input('Enter something:')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small')
        continue

