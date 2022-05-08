a=[6,7,0,8,0,3,3,0,9,7,0]
b=[]
for i in a:
    if i is 0:
        b.append(i)
        a.remove(i)
print(a+b)        