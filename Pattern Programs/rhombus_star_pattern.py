n = int(input("Enter the number: "))
for i in range(0,n):
    for j in range(1,i+1):
        print(" ",end="")
    for j in range(0,n):
        print("*",end="")
    print()