#  The function max()from exercise 1) and the function max_of_three()from exercise 2) will only work for
# two and three numbers, respectively. But suppose we have a much larger number of numbers, or suppose
# we cannot tell in advance how many they are? Write a function max_in_list()that takes a list of
# numbers and returns the largest one.
def max_in_list(lst):
    l=lst[0]
    n=len(lst)
    for i in range(1,n):
        if lst[i]>l:
            l=lst[i]
    return l
lst=list(map(int,input().split()))
print(max_in_list(lst))