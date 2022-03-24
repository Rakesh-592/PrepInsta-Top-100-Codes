#using recursion
def recursum(sum,num1,num2):
    if num1 > num2:
        return sum
    return num1 + recursum(sum,num1+1,num2)

num1 = int(input())
num2 = int(input()) 
sum = 0 
print(recursum(sum,num1,num2))