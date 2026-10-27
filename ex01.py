name=input("Enter student name:")
n=int(input("Enter number of subjects:"))
marks=[]

for i in range(n):
    mark=float(input(f"Enter mark for subject{i+1}:"))
    marks.append(mark)
    total=sum(marks)
    percentage=total/n
    grades={
        90:("A+","Outstanding"),
        80:("A","Excellent"),
        70:("B","Very Good"),
        60:("c","Good"),
        50:("D","Average"),
        40:("F","Needs Improvement")
    }
    for cutoff in grades:
        if percentage>=cutoff:
            grade,performance=grade[cutoff]
            break
        print("\n---Academic Performace---")
        print("Student Name:",name)
        print("Total Marks:",total)
        print("Percentage:",round(percentage,2),"%")
        print("Grade:",grade)
        print("Performance:",performance)