# rite a function that takes a character (i.e. a string of length 1) and returns Trueif it is a vowel, False
# otherwise.
def word(s):
    v=["a","e","i","o","u"]
    if s in v:
        return True
    else:
        return  False
s=input()
print(word(s))
