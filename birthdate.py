a=[[1,1,1,1],[1,1,1,1],[1,1,1,1]]
i=0
b=[]
sum=0
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            sum=sum+a[i][j]
            j+=1
    else:
        b.append(a[i])
    i+=1
print(sum)                
            

