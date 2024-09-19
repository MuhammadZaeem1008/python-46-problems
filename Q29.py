# . Using the higher order function filter(), define a function filter_long_words()that takes a list of
# words and an integer nand returns the list of words that are longer than n.
def filter_longer_words(lst,n):
    ans=list(filter(lambda a:len(a)>n,lst))
    print(ans)
lst=input().split()
n=int(input())
filter_longer_words(lst,n)
