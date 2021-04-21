""" for loop into while loop"""
"""p = 0
for k in range(5, 19, 3):
    print("k=", i)
    p = p + k
else:
    print(k * 2)
print(p)
"""

k = 5
p = 0
while k <= 19:
    print("k = ", k)
    p = p + k
    k = k + 3
else:
    k = k - 3
    print(k * 2)
print("p=", p, end=" ")
"""after ending the loop in for loop 
    the counter always is the last acceptable number which is 17,
     but in while loop we added 3 to the counter 
    manually so after ending while loop the counter 
    has its last modification value which is 20. 
    that's why we should decrease k by three in line print(k*2). 
    also the line else: is redundant, so you can omit it."""