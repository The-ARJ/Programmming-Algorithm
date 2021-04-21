n = 4
num = 65
for i in range(n):
    for j in range(i, n):
        a = chr(num)
        print(a, end=" ")
        num = num+1
    print(" ")
