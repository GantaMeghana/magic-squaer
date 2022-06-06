n=[[2,7,6],
   [9,5,1],
   [4,3,8]]
# i=0
# r1=0
# r2=0
# r3=0
# while i<len(n):
#     j=0
#     while j<len(n[i]):
#         if i==0:
#             r1=r1+n[i][j]
#         elif(i==1):
#             r2=r2+n[i][j]
#         else:
#             r3=r3+n[i][j]
#         j=j+1
#     i=i+1
# if r1==r2==r3:
#     print(r1)
#     print(r2)
#     print(r3)
# else:
#     print("not equel",r1,r2,r3)
# c1=0
# c2=0
# c3=0
# i=0
# while i<len(n):
#     j=0
#     while j<len(n[i]):
#         if j==0:
#             c1=c1+n[i][j]
#         elif j==1:
#             c2=c2+n[i][j]
#         else:
#             c3=c3+n[i][j]
#         j=j+1
#     i=i+1
# if c1==c2==c3:
#     print(c1)
#     print(c2)
#     print(c3)
# else:
#     print("not equel",c1,c2,c3)
# r1=0
# r2=0
# r3=0
# i=0
# while i<len(n):
#     j=0
#     while j<len(n[i]):
#         if i==0:
#             if j==0:
#                 r1=r1+n[i][j]
#             if j==1:
#                 r2=r2+n[i][j]
#             if j==2:
#                 r3=r3+n[i][j]
#                 break
#         elif(i==1):
#             if j==0:
#                 r1=r1+n[i][j]
#             if j==1:
#                 r2=r2+n[i][j]
#             if j==2:
#                 r3=r3+n[i][j]
#                 break
#         elif i==2:
#             if j==0:
#                 r1=r1+n[i][j]
#             if j==1:
#                 r2=r2+n[i][j]
#             if j==2:
#                 r3=r3+n[i][j]
#                 break
#         j=j+1
#     i=i+1
# print(r1,"r1",r2,"r2",r3,"r3")
# d1=0
# d2=0
# i=0
# while i<len(n):
#     j=0
#     while j<len(n[i]):
#         if i==0:
#             if j==0:
#                 d1+=n[i][j]
#             if j==2:
#                 d2+=n[i][j]
#                 break
#         elif i==1:
#             if j==1:
#                 d1+=n[i][j]
#             if j==1:
#                 d2+=n[i][j]
#                 break
#         elif i==2:
#             if j==2:
#                 d1+=n[i][j]
#             if j==0:
#                 d2+=n[i][j]
#                 break
#         j+=1
#     i+=1
# print(d1,d2,"d2")
# # if d1==d2:
# #     print("dioganls",d1)
# #     print("dioganal",d2)
# #     print("it is a magic squere")
# # else:
# #     print("not a magic squere",d1,d2)


n=[[8,3,4],
   [1,5,9],
   [6,7,2]]
r1=0
r2=0
r3=0
i=0
while i<len(n):
    j=0
    while j<len(n[i]):
        if i==0:
            r1=r1+n[i][j]
        elif i==1:
            r2=r2+n[i][j]
        else:
            r3=r3+n[i][j]
        j+=1
    i+=1
if r1==r2==r3:
        print("row1",r1)
        print("row2",r2)
        print("row3",r3)
else:
    print("not equal",r1,r2,r3)
c1=0
c2=0
c3=0
i=0
while i<len(n):
    j=0
    while j<len(n[i]):
        if i==0:
            c1=c1+n[i][j]
        elif i==1:
            c2=c2+n[i][j]
        else:
            c3=c3+n[i][j]
        j+=1
    i+=1
if c1==c2==c3:
    print("column1",c1)
    print("column2",c2)
    print("column3",c3)
else:
    ("not equal",c1,c2,c3)
d1=0
d2=0
i=0
while i<len(n):
    j=0
    while j<len(n[i]):
        if i==0:
            d1=d1+n[i][j]
        elif i==1:
            d2=d2+n[i][j]
        j+=1
    i+=1
if d1==d2:
    print("diagonal1",d1)
    print("diagonal2",d2)
    print("yes it's a magic square")
else:
    ("not equal",d1,d2)


