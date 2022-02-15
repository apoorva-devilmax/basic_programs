num = int(input("Enter a number: "))
if num < 2:
    print("Please enter number greater than or equal to 2")
else:
    primeFlag = True
    for i in range(2, num):
        if num%i == 0:
            primeFlag = False
    if primeFlag:
        print("Entered number", num, "is a prime number")
    else:
        print("Entered number", num, "is not a prime number")