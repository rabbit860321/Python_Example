#__init__作為第一個函式
#每個函式必定以self作為第一個參數
class Employee:
    empCount = 0
    
    def __init__(self,name,salary):  #salary = 薪水
        self.name = name
        self.salary = salary
        Employee.empCount += 1       #每次新增物件count+1

    def displayEmployee(self):
        print("Name:",self.name,",Salay:",self.salary)

emp1 = Employee('阿明',25000)
emp2 = Employee('小美',50000)

emp1.displayEmployee()
emp2.displayEmployee()

print('總員工數:',Employee.empCount)
#----封裝----
class Rectangle:
    def __init__(self,length,width):
        if length <= 0 or width <= 0:
            raise ValueError('長度與寬度不可為負值!') #利用raise來主動引發錯誤ValueError
        self.length = length
        self.width = width

    def perimeter(self):             #周長
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

rect = Rectangle(4,2)

print('* Length = ',str(rect.length),'公尺')
print('* Width = ',str(rect.width),'公尺')
print('* 矩形的周長 = ',str(rect.perimeter()),'公尺')
print('* 矩形的面積 = ',str(rect.area()),'平方公尺')
#----繼承----
class Animal:
    def __init__(self,name):
        self.name = name
    def run(self):
        print(self.name,'runs')
    def jump(self):
        print(self.name,'jumps')
        
class Cat(Animal):         #Cat類別繼承Animal類別
    def shout(self):
        print('喵喵!')

class Dog(Animal):
    def shout(self):
        print('汪汪!')

myCat = Cat('Kitty')
myDog = Dog('Paul')

myCat.run()
myCat.jump()
myCat.shout()

myDog.run()
myDog.jump()
myDog.shout()
#----多型----
class Animal:
    def __init__(self,name):
        self.name = name
    def run(self):
        print(self.name,'runs')
    def jump(self):
        print(self.name,'jumps')
    def talk(self):
        raise NotImplementedError('* 子類別必須實作abstract method')

class Cat(Animal):
    def talk(self):
        return '喵喵!'

class Dog(Animal):
    def talk(self,volume):
        if volume == 1:
            return '小聲汪汪!'
        elif volume == 2:
            return '大聲汪汪!'
        elif volume == 3:
            return '狂吠汪汪!'
        else:
            return '狗狗不叫!'

dog = Dog('Paul')
cat = Cat('Kitty')

print(dog.name,":",dog.talk(0))
print(dog.name,":",dog.talk(1))
print(dog.name,":",dog.talk(2))
print(dog.name,":",dog.talk(3))
print(cat.name,":",cat.talk())
