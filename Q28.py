# Write a function find_longest_word()that takes a list of words and returns the length of the longest
# one. Use only higher order functions.
from functools import reduce
def find_longest_word(lst):
    new=(reduce(lambda a,b:a if len(a)>len(b) else b, lst))
    print(type(new))
    return new
lst=input().split()
print(find_longest_word(lst))