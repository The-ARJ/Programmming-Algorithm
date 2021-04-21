def sum(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum(lst[1:])


lst = [2, 4, 6, 8]
print(sum(lst))
