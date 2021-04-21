# by using While loop
# 1
i = 1
while i <= 4:
    print("* " * i)
    i = i + 1

# 2
i = 1
while i <= 5:
    print("*"*i)
    i = i + 1


# by using For loop
n = 5
i = 1
for i in range(n):
    for j in range(i):
        print("*",end=" ")
    print()
