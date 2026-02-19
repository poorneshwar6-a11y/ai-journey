def calculator(num1,num2,operator):
    if operator==1:
        return num1+num2
    elif operator==2:
        return num1-num2
    elif operator==3:
        return num1*num2
    elif operator==4:
        if num2==0:
            return "cannot divide by zero"
        return num1/num2
while True:
    print("...calculator menu...\n1 Add\n2 Substract\n3 Multiply\n4 Divide\n5 Exit\n")
    operator=int(input("choose:"))
    if operator==5:
        print("exiting calculator")
        break
    num1=int(input("enter first number:"))
    num2=int(input("enter second number:"))
    print("result is:",calculator(num1,num2,operator))