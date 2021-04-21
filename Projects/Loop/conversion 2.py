"""

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

"""
n = 6
for i in range(1, n):
    for j in range(1,i):
        print(j, end=" ")
    print(i)
