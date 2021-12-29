class A:
    classvar1="I am a class variable of class A"

    def __init__(self):
        self.var1="I am inside class A costructor"
        self.classvar1="I am new classvar1 in A"
        self.special="special"

    def func(self):
         print("I am here to check whether super() works fine or not")
class B(A):
     classvar1="I am a class variable of class B"
     def __init__(self):
         super().__init__()
         self.var1 = "I am inside class B costructor"
         self.classvar1 = "I am new classvar1 in B"
         print(super().classvar1)
         print(super().func())

     def func2(self):
         print("Hey")
         print(super().func())

a=A()
b=B()

# print(a.classvar1)S

# print(b.classvar1)
# print(b.special)

b.func2()
