# In English, the present participle is formed by adding the suffix ­ing to the infinite form: go ­> going. A simple
# set of heuristic rules can be given as follows:
# 1. If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
# 2. If the verb ends in ie, change ie to y and add ing
# 3. For words consisting of consonant­vowel­consonant, double the final letter before adding ing
# 4. By default just add ing
def presnt_participle(word):
    lst=["be","flee","see","knee"]
    v=["a","e","i","o","u"]
    if word.endswith("ie"):
        print(word[::-1])
        word=word[:-2] +"y"+"ing"
    elif word.endswith("e") and word not in lst:
        word=word[:-1]+"ing"
    elif word[-3] not in v and word[-2] in v and word[-1]  not in v:
        word=word+word[-1]+"ing"

    return word
word=input()
print(presnt_participle(word))