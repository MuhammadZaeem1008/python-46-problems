# Write a function char_freq()that takes a string and builds a frequency listing of the characters contained
# in it. Represent the frequency listing as a Python dictionary. Try it with something like
# char_freq("abbabcbdbabdbdbabababcbcbab")
def char_freq(str1):
    dict1={}
    for i in str1:
        if i  in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1
    print(dict1)
    for i in dict1.keys():
        print(f"{i} , {dict1[i]}")
str1=input()
char_freq(str1)    



