
def sum(n):
    sum1=0
    if n>0:
        sum1=sum1+n
        sum(n-1)
    print(sum1)

sum(10)