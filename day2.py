#AGE CATEGORY

age=int(input("enter your age:"))
if(0<=age<=12):
    print("child")
elif(13<=age<=19):
    print("teenager")
elif(20<=age<=64):
    print("Adult")
else:
    print("senior")

#GRADE CALCULATOR

marks=int(input("enter your marks:"))
if(90<=marks<=100):
    print("you got 'A' grade")
elif(80<=marks<=89):
    print("you got 'B'grade")
elif(70<=marks<=79):
    print("you got 'C'grade")
elif(60<=marks<=69):
    print("you got 'D'grade")
else:
    print("you got F grade")
    

#EVEN OR ODD

num=int(input("enter the number:"))
if(num%2==0):
    print(num,"is even")
else:
    print(num,"is odd")

#TEMPERATURE ADVICE

temp=int(input("enter the temperature:"))
if(temp<32):
    print("wear a heavy coat")
elif(32<=temp<=50):
    print("Wear a jacket")
elif(51<=temp<=70):
    print("Wear a light sweater")
else:
    print("T-shirt weather!")


#TRIANGLE VALIDATOR

length1=int(input("enter the length1:"))
length2=int(input("enter the length2:"))
length3=int(input("enter the length3:"))
sum=length1+length2+length3
if(sum==180):
    print("it is a valid triangle")
else:
    print("it is not a valid triangle")
if(sum/3==length1):
    print("Triangle is Equilateral")
elif(length1==length2  or length2==length3 or length1==length3):
    print("Triangle is isosceles")
else:
    print("Triangle is scalene")

#leap year

year=int(input("enter the year:"))
if(year%4==0):
    print("year is leap year")
elif(year%100!=0):
    print("year is leap year")
elif(year%400==0):
    print("year is leap year")
else:
    print("year is not leap year")


#BMI CALCULATOR WITH CATEGORIES

weight=int(input("enter the weight:"))
height=int(input("enter the height:"))
bmi=weight/(height**2)
if(bmi<18.5):
    print("Underweight")
elif(18.5<=bmi<=24.9):
    print("Normal weight")
elif(25<=bmi<=29.9):
    print("Overweight")
else:
    print("Obese")

#QUADRANT IDENTIFIER

x=int(input("enter x coordinates:"))
y=int(input("enter y coordinates:"))
if(x>0 and y>0):
    print("1st quadrant")
elif(x<0 and y>0):
    print("2nd quadrant")
elif(x<0 and y<0):
    print("3rd quadrant")
else:
    print("4th quadrant")

#TAX CALCULATOR

money=int(input("enter your amount {$}:"))
if(money<=10000):
    print("no tax to paid")
elif(10001<=money<=30000):
    tax=(money*10)/100
    print(tax,"amount to be paid as tax")
elif(30001<=money<=89000):
    tax=(money*20)/100
    print(tax,"amount to be paid as tax")
else:
    tax=(money*30)/100
    print(tax,"amount to be paid as tax")


