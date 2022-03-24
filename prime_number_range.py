first = int(input()) 
second = int(input()) 
for i in range(first,second+1):
    flag = 1 
    for j in range(2, (i//2)+1):
        if i%j == 0:
            flag = 0
            break 
    if flag == 0 and i != 1:
        print("Prime Number",i)