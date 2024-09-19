# A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in either the written
# record of a language, the works of an author, or in a single text. Define a function that given the file name of
# a text will return all its hapaxes. Make sure your program ignores capitalization.
def hapax(f_name):
    with open(f_name ,"r")as f:
        lines=f.read().split()
        lst=[]
        
        dict1={}
        print(lines)
        for i in lines:
            if  i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        print(dict1)
        hapax=[word for word,count in dict1.items() if count==1]
        print(hapax)
f_name="Q36.txt"
hapax(f_name)