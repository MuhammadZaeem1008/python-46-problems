# Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god",
# "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"}and
# use it to translate your Christmas cards from English into Swedish. Use the higher order function map()to
# write a function translate()that takes a list of English words and returns a list of Swedish words.
dict1= {"merry":"god",
 "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}
def translate(sentence):
    new=list(map(lambda word:dict1[word],sentence))
    return new
sent=input().split()
print(translate(sent))