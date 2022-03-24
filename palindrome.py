num = int(input()) 
temp = num 
reverse = 0 
while(num > 0):
    remainder = num % 10 
    reverse = (reverse * 10) + remainder
    num = num // 10 

if temp == reverse:
    print("Given number {} is Palindrome {}".format(temp,reverse))
else:
    print("Given number{} is not a palindrome".format(temp)) 