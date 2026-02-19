def fact(num):
    if(num<0):
        return "factorial is not defined for negative numbers"
    result=1
    for i in range(1,num+1):
            result*=i
    return result
num=int(input("enter the number to print:"))
print("factorial of",num,"is:",fact(num))
