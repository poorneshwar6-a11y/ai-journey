num=int(input("enter no. of elements:"))
numbers=[]
for i in range(num):
    element=int(input(f"enter element {i+1}:"))
    numbers.append(element)
print("list is:",numbers)
even=0
for n in numbers:
    if(n%2==0):
        even=even+1
print("no. of even numbers in list is:",even)
print("no. of odd numbers in list is:",num-even)
