"""WAP  to find factorial of number by using a function?"""


def factorial(num):
    product = 1
    for i in range(2, num + 1):
        product = product * i
    return product


num = int(input("Enter a number for factorial:"))
factorial(num)
print("The factorial is:", factorial(num))
