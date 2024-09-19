# rite a function filter_long_words()that takes a list of words and an integer nand returns the list of
# words that are longer than n.
def filter_long_words(lst,n):
    lst2=[]
    for i in lst:
        if len(i)>n:
            lst2.append(i)
    return lst2
lst=input().split()
n=int(input())
print(filter_long_words(lst,n))