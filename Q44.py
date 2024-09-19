# Your task in this exercise is as follows:
# Generate a string with N opening brackets ("[") and N closing brackets ("]"), in some arbitrary order.
# Determine whether the generated string is balanced; that is, whether it consists entirely of pairs of
# opening/closing brackets (in that order), none of which mis­nest.
# Examples:
# [] OK ][ NOT OK
# [][] OK ][][ NOT OK
# [[][]] OK []][[] NOT OK
def chk_order(string):
    stack=[]
    for i in string:
        if i=="[":
            stack.append(i)
        elif(i=="]"):
            if  len(stack)==0:
                print("given string is not ordered")
                return False
            stack.pop()
    if len(stack)==0:
        print("given string is ordered")
    else:
        print("given string is not ordered")
string=input()
chk_order(string)