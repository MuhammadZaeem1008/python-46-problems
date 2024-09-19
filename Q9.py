#  Write a function is_member()that takes a value (i.e. a number, string, etc) xand a list of values a, and
# returns Trueif xis a member of a, Falseotherwise. (Note that this is exactly what the inoperator does,
# but for the sake of the exercise you should pretend Python did not have this operator.)
def is_member(x,a):
    for i in a:
        if  x==i:
            return True
    return False
x=int(input())
a=list(map(int,input().split()))
print(is_member(x,a))
