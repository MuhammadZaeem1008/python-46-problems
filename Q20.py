# Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god",
# "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"}and
# use it to translate your Christmas cards from English into Swedish. That is, write a function translate()
# that takes a list of English words and returns a list of Swedish words.
def translate(lst):
    dict1= {"merry":"god",
 "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}
    lst2=[]
    for i in lst:
        lst2.append(dict1[i])   
    return lst2
lst=input().split()
print(translate(lst))