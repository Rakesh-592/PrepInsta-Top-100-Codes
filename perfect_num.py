num = int(input("Enter the Number:"))
sum = 0 
for i in range(1,num):
    if(num %i == 0):
        sum += i

if(sum == num):
    print("The Num is a Perfect Number")
else:
    print("The Num is not a Perfect Number")
