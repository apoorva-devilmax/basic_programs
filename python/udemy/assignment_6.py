num = int(input("Enter a number: "))
for x in range(num):
    if x%10 == 0:
        continue
    if x > 100:
        break
    print(x)
