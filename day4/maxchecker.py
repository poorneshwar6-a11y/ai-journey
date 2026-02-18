def check(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
a=int(input("enter number 1:"))
b=int(input("enter number 2:"))
c=int(input("enter number 3:"))
print("greatest number is:",check(a,b,c))
