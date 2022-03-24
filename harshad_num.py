n = int(input())
p = n #duplicate the n
l = []
sum1 = 0
while(n > 0):
    x = n%10
    l.append(x)
    n = n//10
sum1 = sum(l)
if(p%sum1 == 0):
    print("Harshad Number")
else:
    print("Not Harshad Number")

