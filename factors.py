num = int(input("Enter the Number:")) 
for i in range(1,num+1):
    if(num%i == 0):
        print(i, end=" ")