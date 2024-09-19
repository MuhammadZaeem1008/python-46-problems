 #Define a function max()that takes two numbers as arguments and returns the largest of them.
 #  Use the ifthen­else construct available in Python.
 #  (It is true that Python has the max()function built in, but writing it
#yourself is nevertheless a good exercise.
def max(a,b):
    if a>b:
        return a
    else:
        return b
a,b=list(map(int,input().split()))
res=max(a,b)
print(a)
