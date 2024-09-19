
# . Define a function sum()and a function multiply()that sums and multiplies (respectively) all the
# numbers in a list of numbers. For example, sum([1, 2, 3, 4])should return 10, and multiply([1,
# 2, 3, 4])should return 24.
def sum(a):
    num=0
    for i in a:
        num+=i
    return num
def multiply(a):
    num=1
    for i in a:
        num*=i
    return num
lst=list(map(int,input().split()))
print(sum(lst))
print(multiply(lst))
