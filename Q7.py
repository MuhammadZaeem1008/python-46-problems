# Define a function reverse()that computes the reversal of a string. For example, reverse("I am
# testing")should return the string "gnitset ma I".
def reverse(str1):
    lst=[]
    for i in str1:
        lst.append(i)
    lst.reverse()
    return "".join(lst)

str1=input()
print(reverse(str1))