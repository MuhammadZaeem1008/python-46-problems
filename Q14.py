#  Write a program that maps a list of words into a list of integers representing the lengths of the correponding
# words.
def find_len(lst):
    lst3=list(map(lambda x:len(x),lst))
    print(lst3)
lst=input().split()
print(lst)
find_len(lst)
