lst = [1, 2, 3]

def iterate(lst, l = len(lst)):
    i = l - 1 
    if 0 > i:
        return 0
    print(lst[i])
    iterate(lst, i)

iterate(lst)