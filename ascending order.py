# date=input("Enter your date/month:")
# b=0
# c=0
# if date!="-":
#     if len(date)<=3:
#         if date[0:1]>="1" and date[0:1]<"9":
#             b=(int(date[0:1])+1)
#             c=date[2:]
#     else:
#         if date[0:2]>="1" and date[0:2]<"30":
#             b=(int(date[0:2])+1)
#             c=date[3:]
#         if (date[0:2]=="31" or date[0:2]=="30") and date[3:]=="12":
#             b="1"
#             c="1"
#         elif (date[0:2]=="31" or date[0:2]=="30" )and date[3:]!="12":
#             b="1"
#             c=(int(date[3:])+1)
#         else:
#             print("month is not define")
# print(b,c)


date=int(input("enter the number"))
month=int(input("enter the number"))
year=int(input("enter the number"))
print(date+1,"/",month,"/",year)
    
