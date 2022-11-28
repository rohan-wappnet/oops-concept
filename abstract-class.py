from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    def __init__(self):
        self.length = 8
        self.breadth = 9

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())