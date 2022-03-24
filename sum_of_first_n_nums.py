"""num = int(input())
sum = 0
for i in range(num+1):
    sum += i
print(sum)"""

#using recursion
def getSum(num):
    if(num == 1):
        return 1
    return num + getSum(num-1)

num = 5
print(getSum(num))