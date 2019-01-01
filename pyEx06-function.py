def sumCart():
    totalCost = cost1 + cost2
    print("TotalCost = ",totalCost)

def sumCart1(item1,item2):
    totalCost = item1 + item2
    print("TotalCost = ",totalCost)

def sumCart2(item1,item2):
    totalCost = item1 + item2
    return totalCost

def factorial(n):
    if n ==  0 or n == 1:
        return 1
    else:
        return (n * factorial(n-1))

cost1 = 15
cost2 = 20

sumCart()
sumCart1(cost1,cost2)

total = sumCart2(cost1,cost2)
print("TotalCost = ",total)

n = int(input('階層:'))
print(factorial(n))
