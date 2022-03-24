num = int(input())
temp = num 
reverse = 0 
while num > 0:
    remainder = num % 10 
    reverse = (reverse * 10) + remainder #formula
    num = num // 10 

print("The given num is {} and reverse is {}".format(temp,reverse))
#rev = str(num)[::-1]
#print(rev)