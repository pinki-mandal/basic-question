# a=[5,6,2,7,1]
# num=int(input("enter the number"))
# i=0
# count=0
# while i<len(a):
#     if a[i]>num:
#         if count==0:
#             m=a[i]
#         count+=1
#     i+=1
# print(m)        
            
        
a=[2,3,6,6,5]
num=int(input("enter the number"))
i=0
count=0
while i<len(a):
    if a[i]<num:
        if count==0:
            m=a[i]
        count+=1
    i+=1
print(m)        
            
        
        