#guessing number
computer=10
while True :
    num=int(input("enter he value"))
    if(num>computer):
        print("Guess is too high")
    elif(num<computer):
        print("Guess is too low")
    else:
        print("your correct")
        break
