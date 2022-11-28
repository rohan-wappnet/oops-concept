class Shape:
    data1 = "abc"

    def no_of_sides(self):
        print("My sides need to be defined. I am from shape class.")

    def two_dimensional(self):
        print("I am a 2D object. I am from shape class")


class Square(Shape):
    data2 = "xyz"

    def no_of_sides(self):
        print("I have 4 sides. I am from Square class")

    def color(self):
        print("I have teal color. I am from Square class.")


sq = Square()

sq.no_of_sides()

sq.two_dimensional()

sq.color()
print("Old value of data1 = ", sq.data1)

sq.data1 = "New value"
print("The value of data1 in Shape class overridden by the Square class = ", sq.data1)
