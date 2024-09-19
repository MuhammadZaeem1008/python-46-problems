# Write a program that will calculate the average word length of a text stored in a file (i.e the sum of all the
# lengths of the word tokens in the text, divided by the number of word tokens).
def avg_words_length(f_name):
    with open(f_name,"r")as f:
        names=f.read().split()
        
        print(names)
        sum=0
        count=0
        for name in names:
            sum+=len(name)
            count+=1
        print(sum)
        avg=sum/count
        print(avg)
f_name="Q38.txt"
avg_words_length(f_name)