#MULTIPLICATION TABLE

#USING FOR LOOP
num=int(input("enter number for table:"))
for i in range(11):
    print(num, "X", i, "=",num*i)

#USING WHILE LOOP
num=int(input("enter number for table:"))
i=1
while(i<=10):
    print(num, "X", i, "=",num*i)
    i+=1    