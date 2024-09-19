# . Write a version of a palindrome recogniser that accepts a file name from the user, reads each line, and
# prints the line to the screen if it is a palindrome.
def palindrome_recongniser(f_name):
    with open(f_name,"r")as f:
        lines=f.read().splitlines()
        print(lines)
        for  line in lines:
            if line==line[::-1]:
                print(f"{line} \n is a palindromic line")
            else:
                print(f"{line} >>>>> not palindrome")
f_name="Q32.txt"
palindrome_recongniser(f_name)