import random
my_list = []
while i<50:
    num = random.randint(1,200)
    if num % 2 == 0:
        my_list.append(num)
        i=i+1