num=int(input("enter no. of elements:"))
numbers=[]
for i in range(num):
    element=int(input(f"enter element {i+1}:"))
    numbers.append(element)
print("list is:",numbers)
max=numbers[0]
for i in range(1,len(numbers)):
    if(numbers[i]>max):
        max=numbers[i]
print("maximum number is:",max)