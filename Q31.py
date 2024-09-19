#map
def maps(double,lst):
    res=[]
    for i in lst:
        res.append(double(i))
    return res
def filter(even,lst):
    res=[]
    for i in lst:
        if even(i) :
            res.append(i)
    return res
def double(x):
    return x*2
def even(x):
     
    return x%2==0
lst=[1,2,3,4,5,6]
print(maps(double,lst))
print(filter(even,lst))
def reduce(func,lst):
    for i in lst:
        
