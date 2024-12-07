from functools import cmp_to_key
orders = [1,4,6,7,8,5]
rules = {
    4 : (1)
}

def cmp(a,b):
    if a < b:
        return 1
    elif a > b:
        return -1
    return 0
x = sorted(orders, key=cmp_to_key(cmp))
print(x)