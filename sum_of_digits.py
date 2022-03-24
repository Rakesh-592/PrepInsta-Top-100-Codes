#using string char extraction
""""
num = input("enter no ")
sum = 0

for i in num:
    sum = sum + int(i)
print(sum)"""

#using brute force approach
"""
num = 1223
sum = 0
while num!=0:
    digit = int(num%10)
    sum += digit
    num /= 10
print(sum)"""

#using map(),sum(),strip()
def getSum(n):
    num_string = str(n) #convert to string

    list_of_num = list(map(int,num_string.strip()))
    print(list_of_num)
    return sum(list_of_num) 
n = int(input())
print(getSum(n))