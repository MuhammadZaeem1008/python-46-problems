# An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a
# new word or phrase, using all the original letters exactly once; e.g., orchestra = carthorse. Using the word
# list at http://www.puzzlers.org/pub/wordlists/unixdict.txt, write a program that finds the sets of words that
# share the same characters that contain the most words in them.
def anagram():
    lst=["orchestra","carthorse","enlist","stone","silent","listen"]
    new=lst[0]
    n=len(lst)
    for i in range(1,n):
        for j in lst[i]:
            if j not in new:
                new=lst[i]
                
                break
            else:
            
anagram()


                
