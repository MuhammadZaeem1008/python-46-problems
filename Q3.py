# . Define a function that computes the length of a given list or string. (It is true that Python has the len()
# function built in, but writing it yourself is nevertheless a good exercise.)
def find_len(a):
    count=0
    for i in a:
        count+=1
    return count
a=input()
print(find_len(a))