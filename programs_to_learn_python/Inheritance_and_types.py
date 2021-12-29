"""
Inheritance = The method of one class aquaring the properties of other class...
*Types:
Single inheritance
Multiple inheritance
Multilevel inheritance
"""
#Single inheritance
"""
class Employee:
    salary =40000

    def __init__(self,name,age,roll):
        self.name = name
        self.age = age
        self.roll = roll

    def printdetails(self):
        print(f"The name is {self.name} and the age is {self.age} and the profession is {self.roll}")

class Player(Employee):
    salary =30000
    def printdetails(self):
        print(f"The name is {self.name} and the age is {self.age} and the profession is {self.roll} and he is a good player")

karthik=Employee("karthik",19,"Android-developer")
karthik.printdetails()

shreya=Player("shreya",20,"programmer")
shreya.printdetails()
"""

#multiple inheritance
class Employee:
    salary =40000

    def __init__(self,name,age,roll):
        self.name = name
        self.age = age
        self.roll = roll

    def printdetails(self):
        print(f"The name is {self.name} and the age is {self.age} and the profession is {self.roll}")

class Player:
    def __init__(self, name,game):
        self.name = name
        self.game = game

    def printdetails(self):
        print(f"The name is {self.name} and the game is {self.game}")

class CoolProgrammer(Employee,Player):
    language =["python","c++","java"]
    def print_lang(self):
        print(f"The language is {self.language}")

# Karthik=CoolProgrammer("karthik",19,"Android-developer")
# # print(type(Karthik))
# print(Karthik.salary)
# print(Karthik.printdetails())
bvc=Player("bvc","football")
# print(bvc.salary)
print(bvc.printdetails())


#Multilevel inheritance

# class Dad:
#     basketball=1
#     def fun_dance(self):
#         return "Mai nagin nagin nagin nagin "
#
# class Son(Dad):
#     cricket=1
#     # basketball=3
#
#     def fun_dance(self):
#         return "I like to move it , move it"
#
# class Grandson(Son):
#     chess=3
#
#     def fun_dance(self):
#         return "Mai nashe mai yaa mujme nasha haii"
#
# shreya=Dad()
# poonki=Son()
# karthik=Grandson()
# print(karthik.fun_dance())
# print(shreya.fun_dance())
# print(poonki.fun_dance())
#
# print(karthik.chess)
# print(karthik.basketball)