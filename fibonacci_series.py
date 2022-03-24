from tkinter import N


def fib(n):
    if(n<2):
        return n 
    fs = [0,1] 
    for i in range(1,n):
        fs.append(fs[i] + fs[i-1])
    return fs[n] 

n = 6 
print(fib(n))

#there is an error in this code check to solve later