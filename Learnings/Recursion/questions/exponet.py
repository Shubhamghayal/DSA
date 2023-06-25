def pow(m,n):
    if n==0:
        return 1
    else:
        return pow(m,n-1)*m
    
print(pow(2,5))