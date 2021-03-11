"""
Write a program to take a input from the user, ask the
user age. If the user age is below 15 print a message 'you are child',
if user age is greater than 15 and lesser than 40 print a message
'you are adult',if the user age is greater than 40 then print a message
'you are old'
 """

age = int(input("enter your age:"))
if age < 15:
    print("you are child")
elif age > 15 and age < 40:
    print("your are adult")
else:
    print("you are old")


