def factorial():
    num = int(input("Enter a number for factorial:"))
    product = 1
    for i in range(2, num + 1):
        product = product * i
    print("The factorial is:", product)


factorial()
