base = int(input("Enter Base Number:"))
expo = int(input("Enter Expo Number:"))
temp = 1 

for i in range(0,expo):
    temp = temp * base 
print(temp)