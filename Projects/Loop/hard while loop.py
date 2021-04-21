# 2
i = 1
j = 2
while i >= 1:
    a = " " * j + "*" * i + " " * j
    print(a)
    i = i + 2
    j = j - 1
    if i > 5:
        break
i = 3
j = 1
while i >= 1:
    a = " " * j + "*" * i + " " * j
    print(a)
    i = i - 2
    j = j + 1
