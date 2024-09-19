# 3. Define a simple "spelling correction" function correct()that takes a string and sees to it that 1) two or
# more occurrences of the space character is compressed into one, and 2) inserts an extra space after a
# period if the period is directly followed by a letter. E.g. correct("This is very funny and
# cool.Indeed!")should return "This is very funny and cool. Indeed!"Tip: Use regular
# expressions
def spelling_correction(str1):
    re=[]
    chk_space=str1[0]
    n=len(str1)
    for i in range(1,n):
        if str1[i]==" " and chk_space==" ":
            pass
        else:
           re.append(chk_space)
           chk_space=str1[i]
    re.append(chk_space)
    res="".join(re)
    n=len(res)
    for i in range(n):
        result=[]
        result.append(res[i])
        if res[i]=="." and i+1<n and res[i+1].isalpha():
            result.append(" ")
    print("".join(result))
    # chk_dot=res[0]
    # print(res[0])
    # for i in range(1,na):
    #     result=[]
    #     if  res[i].isalpha() and chk_dot==".":
    #         result.append(" ")
    #         # result.append(res[i])

    #         # print(result)
    #         chk_dot=res[i]
    #     else:
    #         chk_dot=res[i]
    #         result.append(res[i])
    # print(result)
    #         # print(res[i])
    # print("".join(result))


str1=input("")
spelling_correction(str1)
    