import math 
first, second = 150, 160 

def is_Armstrong(val:int) -> bool:
    sum = 0 
    num = [int(d) for d in str(val)]
    for i in range(0,len(num)):
        sum = sum + math.pow(num[i], len(num))

    if(sum == val):
        print("{} number is Armstrong".format(val))
    else:
        print("{} number is not Armstrong".format(val))

for i in range(first,second + 1):
    is_Armstrong(i)