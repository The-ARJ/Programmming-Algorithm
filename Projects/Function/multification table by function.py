def multiplication():
    num = int(input("Enter a number:"))
    n = 11
    for i in range(1, n, 1):
        product = num * i
        print(num, "*", i, "=", product)


multiplication()
