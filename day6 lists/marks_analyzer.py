students=int(input("enter no. of students:"))
marks=[]
for i in range(students):
    mark=int(input(f"enter marks of student {i+1}:"))
    marks.append(mark)
print("Marks list is:",marks)
total_marks=sum(marks)
average=total_marks/students
highest=marks[0]
lowest=marks[0]
for i in range(1,len(marks)):
    if(marks[i]>highest):
        highest=marks[i]
    if(marks[i]<lowest):
        lowest=marks[i]
print("Total marks is:",total_marks)
print("Average of class is:",average)
print("Highest marks is:",highest)
print("lowest marks is:",lowest)
    