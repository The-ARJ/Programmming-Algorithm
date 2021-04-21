""" Addition, By function having no parameter and no return type """


def add():
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    c = a + b
    print("The Sum is:", c)


add()

"""Subtraction, By function having parameter and no return type"""


def sub(a, b):
    c = a - b
    print("The sub is:", c)


a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
sub(a, b)

"""Multiplication, By function having no parameter and with return type"""


def mul():
    c = a * b
    return c


a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
ans = mul()
print("The mul is:", ans)

"""Division, By function having parameter and with return type"""


def div(a, b):
    c = a / b
    return c


a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
ans = div(a, b)
print("The dev is:", ans)
