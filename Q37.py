# Write a program that given a text file will create a new text file in which all the lines from the original file are
# numbered from 1 to n (where n is the number of lines in the file).
def numbering(f_name):
    with open(f_name,"r")as f:
        with open("new_file.txt" ,"w") as n:
            read=f.read().splitlines()
            print(read)
            count=1
            for r in read:
                n.writelines(f"{count} {r}\n")
                count+=1
f_name="Q37.txt"
numbering(f_name)