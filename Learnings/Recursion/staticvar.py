def fun(n):
    if n>0:
        return fun(n-1)+n
    return 0

a=5
print(fun(a))