# e. Write a Python program that, when started 1) randomly picks a word w from given list of
# words, 2) randomly permutes w (thus creating an anagram of w), 3) presents the anagram to the user, and
# 4) enters an interactive loop in which the user is invited to guess the original word. It may be a good idea to
# work with (say) colour words only. The interaction with the program may look like so:
# >>> import anagram
# Colour word anagram: onwbr
# Guess the colour word!
# black
# Guess the colour word!
# brown
# Correct!
import random
def anagram():
    lst=["red","brown","orange","blue","purple"]
    # random.shuffle(lst)
    word=(random.choice(lst))
    print(word)
    a="".join(random.sample(word))
    # ab=random.shuffle(word)
    # print(ab)
    print(a)
    print((f" Colour word anagram  :{a}"))
    while True:
        print("guess the color word ")
        guess=input()
        if  guess==word:
            print("Correct")
            break
anagram()
