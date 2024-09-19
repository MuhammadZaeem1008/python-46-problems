# Write a program that maps a list of words into a list of integers representing the lengths of the correponding
# words. Write it in three different ways: 1) using a for­loop, 2) using the higher order function map(), and 3)
# using list comprehensions.
def using_loop(lst):
    lst2=[]
    for i in lst:
        lst2.append(len(i))
    return lst2
lst=input().split()
print(using_loop(lst))
#using list comprehension
def using_list_comprehension(lst):
    lst2=[len(i) for i in lst]
    print(lst2)
using_list_comprehension(lst)
#using map
def using_map(lst):
    lst2=list(map(len,lst))
    print(lst2)
using_map(lst)