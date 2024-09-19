# Define a function overlapping()that takes two lists and returns True if they have at least one member in
# common, False otherwise. You may use your is_member()function, or the inoperator, but for the sake
# of the exercise, you should (also) write it using two nested for­loops.
def overlapping(lst1,lst2):
    for i in lst1:
        for j in lst2:
            if j==i:
                return True
    return False
lst1=list(map(int,input().split()))
lst2=list(map(int,input().split()))
print(overlapping(lst1,lst2))
