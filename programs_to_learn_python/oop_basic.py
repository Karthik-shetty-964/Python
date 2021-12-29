class Student:
    salary=10000
    pass

karthik=Student()
Shreya=Student()
# print(Shreya)
karthik.name="karthik"
karthik.age=19

Shreya.name="shreya"
Shreya.age=20

karthik.salary=30000
Student.salary=40000

print(karthik.salary)
print(Shreya.salary)

print(Student.__dict__)
print(Shreya.__dict__)
print(karthik.__dict__)