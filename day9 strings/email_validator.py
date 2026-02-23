email=input("enter your email:")
total=0
flag=0
index=email.find("@")
if(index==-1):
    flag=1
after=email[index+1:]
if "." in after:
    flag=0
else:
    flag=1
if(email[0]=="@" or email[-1]=="@"):
    flag=1
for ch in email:
    if(ch==" "):
        flag=1
    elif(ch=="@"):
        total+=1
if(total>1 or flag==1):
    print("your Email is invalid")
else:
    print("your Email is valid")
