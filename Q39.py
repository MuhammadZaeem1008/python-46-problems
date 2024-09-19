import random
lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(random.choice(lst))
print(f"""Hello! What is your name?
Torbjörn
Well, Torbjörn, I am thinking of a number between 1 and 20.""")
n=random.choice(lst)
print(n)
count=1
while True:

    print("Take a guess.")
    num=int(input())
    
    if num>n:
        print("your guess is high ")
        count=count+1
    elif num<n:
        print("your guess is too low")
        count=count+1
    elif num==n:
        print(f"Good job, Torbjörn! You guessed my number in {count} guesses!")
        break
       



# Your guess is too low.
# Take a guess.
# 15
# Your guess is too low.
# Take a guess.
# 18
# Good job, Torbjörn! You guessed my number in 3 guesses!