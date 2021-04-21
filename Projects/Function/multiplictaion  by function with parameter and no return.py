def multiplication(num):
    n = 11
    for i in range(1, n, 1):
        product = num * i
        return product


num = int(input("Enter a number:"))
for i in range (1,11):
    print(num, "*", i, "=", multiplication(num))
