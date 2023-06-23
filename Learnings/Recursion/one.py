# def main(n):
#     if n>0:
#         print(n)
#         main(n-1)
    
    
# x=10
# main(x)


def main(n):
    if n>0:
        main(n-1)
        print(n)
    
    
x=10
main(x)