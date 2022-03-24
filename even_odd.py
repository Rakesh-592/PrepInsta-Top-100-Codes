"""17num = int(input()) 
if(num%2 == 0):
    print("Even")
else:
    print("odd")"""

#using ternary operator
#(True:Action)if(condition)else:(False:Action)
num = int(input())
print("Even") if num%2 == 0 else print("Odd")