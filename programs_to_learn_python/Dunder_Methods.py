# Dunder methods are the special methods that start and ends with '__name__'..These methods usually gets exeucuted on their own at certain statements
class Employee:
    salary =40000

    def __init__(self,name,age,roll):
        self.name = name
        self.age = age
        self.roll = roll

    def printdetails(self):
        print(f"The name is {self.name} and the age is {self.age} and the profession is {self.roll}")

    def __add__(self, other):
        return self.age+other.age
    def __truediv__(self,other):
        return self.age/other.age

    # def __repr__(self):
    #           return f"The name is {self.name} and the age is {self.age} and the role is {self.roll}"
    #
    # def __str__(self):
    #     return "I am better than __repr__  bitches"

emp1=Employee("karthik",33,"Pysch coder")
emp2=Employee("Bvc",38,"Porn star")

print(emp1+emp2)
print(emp1/emp2)

print(emp1)