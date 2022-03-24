import math 
value = int(input("Enter the Number: "))
num = [int(d) for d in str(value)]
sum = 0 
for i in range(0,len(num)):
    sum = sum + math.pow(num[i], len(num))

if sum == value:
    print("Armstrong Number")
else: 
    print("Not an Armstrong Number")