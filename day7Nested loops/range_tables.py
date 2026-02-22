start=int(input("enter first number:"))
end=int(input("enter ending number"))
if(start>end):
    print("invalid range")
for i in range (start,end+1):
    print("Table of ",i,"is:")
    for j in range(1,11):
        print(i,"X",j,"=",i*j)
    print()