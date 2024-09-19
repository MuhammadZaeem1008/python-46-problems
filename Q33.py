# According to Wikipedia, a semordnilap is a word or phrase that spells a different word or phrase backwards.
# ("Semordnilap" is itself "palindromes" spelled backwards.) Write a semordnilap recogniser that accepts a file
# name (pointing to a list of words) from the user and finds and prints all pairs of words that are semordnilaps
# to the screen. For example, if "stressed" and "desserts" is part of the word list, the the output should include
# the pair "stressed desserts". Note, by the way, that each pair by itself forms a palindrome!
def chk_semordinalp(f_name):
    with open(f_name,"r")as f :
        lsts=f.read().split()
        print(lsts)
        for l in lsts:
            n=l.split(",")
        print(n)
        chk=n[0]
        d=len(n)
        for i in n:
            for j in n:
                if i==j[::-1]:
                    print(f" {i}  {j}  ")
f_name="Q33.txt"
chk_semordinalp(f_name)
