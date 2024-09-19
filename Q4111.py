import random
def lingo():
    word_list = ["tiger", "snake", "zebra", "crane", "flute","liger"]
    random_word=random.choice(word_list)
    while True:
        guess=input()
        clue=[]
        indices=[]
        for i in range(len(guess)):
            if guess[i]==random_word[i]:
                clue.append(f"[{guess[i]}]")
                indices.append(i)

            else:
                clue.append(guess[i])   
        for i in range(len(guess)):
            if clue[i]!=f"[{guess[i]}]":
                if guess[i] in random_word:
                    for j in range(len(guess)):
                        if guess[i]==random_word[j] and j not in indices and clue[i]==guess[i]:
                            clue[i]=f"({guess[i]})"
                            indices.append(j)
                            break
        clues="".join(clue)
        print(indices)
        print(f"clue , {clues}")
        if guess==random_word:
            break
lingo()