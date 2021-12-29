class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    @property
    def email(self):
        if(self.fname==None and self.lname==None):
            return "Email is not set..Please set it using setters"
        else:
            return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self,string):
        name=string.split('@')[0]
        self.fname=name.split('.')[0]
        self.lname=name.split('.')[1]
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None

emp1=Employee("Karthik","shetty")
print(emp1.email)
emp1.email="this.that@gmail.com"
print(emp1.email)

del emp1.email
print(emp1.email)