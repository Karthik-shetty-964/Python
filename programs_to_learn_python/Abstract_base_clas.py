
# from abc import ABCMeta,abstractmethod
from abc import ABC, abstractmethod

# class Shape(metaclass=ABCMeta):
#     @abstractmethod
#     def printdetails(self):
#         return 0
#
class Shape(ABC):
    @abstractmethod
    def printdetails(self):
        return 0

class Rectangle(Shape):
    def __init__(self):
        self.length=29
        self.breadth=38

    def printdetails(self):
           return self.length*self.breadth

class Square(Shape):
    def __init__(self):
        self.length=2

    def printdetails(self):
        return self.length**2
# shape1=Shape() # we can not create objects for abstract class
rect1=Rectangle()
square1=Square()
print(square1.printdetails())
# print(rect1.printdetails())