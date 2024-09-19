import random
def lingo():
    my_list=["tiger","snake","liger","zebra"]
    word=random.choice(my_list)
    guess=input("enter your guess")
    print(word)
    while True:
        n=len(guess)
        lst=[]
        for i in range(n):
            if guess[i] in word:
                lst.append(f"[{guess[i]}]")
                if guess.index(guess[i])==word.index(word[i]):
                    lst.append(f"({guess[i]})")
            else:
                lst.append(guess[i])
        new="".join(lst)
        if guess==word:
        
            return False
lingo()
