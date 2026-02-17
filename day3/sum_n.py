#sum of numbers

#USING WHILE LOOP
num=int(input("enter the number to do sum upto it:"))
i=0
sum=0
while(i<=num):
    sum=sum+i
    i=i+1
print("sum is",sum)


#USING FOR LOOP
num=int(input("enter the number to do sum upto it:"))
sum=0
for i in range(num+1):
    sum=sum+i
print("sum is:",sum)
