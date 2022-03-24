def printDivisiors(n,factors):
    i = 1
    while(i <= n):
        if(n%i == 0):
            factors.append(i)
        i += 1
    return sum(factors) - n

def main():
    number1,number2 = 6,28
    if int(printDivisiors(number1, [])/number1) == int(printDivisiors(number2,[])/number2):
        print("Friendly pair")
    else:
        print("Not a Friendly Pair")

if __name__ == "__main__":
    main()

