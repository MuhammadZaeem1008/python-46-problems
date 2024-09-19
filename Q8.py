def palindrome(word):
    
    if word==word[::-1]:
        return True
    else:
        return False
word=input()
print(palindrome(word))
# def plaindrome(word):
#     left=0
#     right=len(word)-1
#     while left<right:
#         if word[left]!=word[right]:
#             return False
#         left+=1
#         right-=1
#     return True
# word=input()
# print(plaindrome(word))