# Write a function translate()that will translate a text into "rövarspråket" (Swedish for "robber's
# language"). That is, double every consonant and place an occurrence of "o"in between. For example,
# translate("this is fun")should return the string "tothohisos isos fofunon".
def translate(text):

    v=["a","e","i","o","u"]
    new=''
    for i in text:
        if i not in v and i!=" ":
            new+=i+"o"+i
        else:
            new+=i
    return new
text=input()
print(translate(text))
