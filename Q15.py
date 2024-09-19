# # Write a function find_longest_word()that takes a list of words and returns the length of the longest
# one.
def find_longest_word(lst):
    lst2=[]
    for  i in lst:
        lst2.append(len(i))
    lst2.sort(reverse=True)
    for i in lst:
        if (len(i)==lst2[0]):
            return i,lst2[0]
    
lst=input().split()
print(find_longest_word(lst))