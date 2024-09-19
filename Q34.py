# . Write a procedure char_freq_table()that, when run in a terminal, accepts a file name from the user,
# builds a frequency listing of the characters contained in the file, and prints a sorted and nicely formatted
# character frequency table to the screen.
def char_freq_table(f_name):
    with open(f_name,"r")as f:
        txt=f.read()
        sorted_txt="".join(sorted(txt))
        print(sorted_txt)
        dict1={}
        for i in sorted_txt:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        for i in dict1.keys():
            print(f"{i} {dict1[i]}")
f_name="Q34.txt"
char_freq_table(f_name)        

            
