# class Employee:
#     def printdetails(self):
#         print(f"The name is {self.name} and the age is {self.age}")
#     pass
#
# karthik=Employee()
# karthik.name="Karthik shetty"
# karthik.age=19
# karthik.printdetails()

#Constructors
class Employee:
    salary=30000
    def __init__(self,name,age,roll):
        self.name=name
        self.age=age
        self.roll=roll

    def printdetails(self):
        print(f"The name is {self.name} and the age is {self.age} and the profession is {self.roll}")

    @classmethod
    def change_salary(cls,new_salary):
        cls.salary=new_salary
        return cls.salary

    #Using class methods as alternative Constructors
    @classmethod
    def alternative_constructor(cls,string):
        # params=string.split("-")
        # return cls(params[0],params[1],params[2])
        #The above code can be done using one liner too
         return cls(* string.split("-"))

    #Statid method - These will not be having any deafault arguements like self or cls
    @staticmethod
    def method_static(string):
        print(f"{string} is a handsome man")



karthik=Employee("Karthik shetty",19,"Android-developer")
# karthik.printdetails()

# print(Employee.salary)
# karthik.change_salary(40000)
# print(Employee.salary)
# print(karthik.salary)

# shreya=Employee.alternative_constructor("Shreya-20-Programmer")
# shreya.printdetails()

karthik.method_static("karthik")



