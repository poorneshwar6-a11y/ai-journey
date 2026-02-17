#sum of numbers

#USING WHILE LOOP
num=int(input("enter the number to do sum upto it:"))
i=0
total=0
while(i<=num):
    total+=i
    i=i+1
print("sum is",total)


#USING FOR LOOP
num=int(input("enter the number to do sum upto it:"))
total=0
for i in range(num+1):
    total=total+i
print("sum is:",total)
