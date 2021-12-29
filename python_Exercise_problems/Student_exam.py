n=int(input("Enter the number of subjects"))
marks=[]

print("Enter the marks of each subject")
for i in range(n):
    marks.append(int(input()))

stud=int(input("Enter the Number of students"))
students=[]
print("Enter maximum credit score for each student")
for i in range(stud):
    students.append(int(input()))
    
# print(marks)
# print(students)
max_credit=max(students)
count=0
for i in range(n):
    if(max_credit>=marks[i]):
        count+=1
    

print(count)
    