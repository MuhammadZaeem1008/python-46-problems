#  Define a function max_of_three()that takes three numbers as arguments and returns the largest of
# them.
def max_of_three(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    else:
        return c
a,b,c=map(int,input().split())
res=max_of_three(a,b,c)
print(res)    
