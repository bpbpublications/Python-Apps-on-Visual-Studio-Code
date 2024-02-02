
class Shape:
    def get_area(self):
        pass

    def get_perimeter(self):
        pass

    def draw(self):
        print("Drawing a shape")


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side * self.side

    def get_perimeter(self):
        return 4 * self.side


#creating object of Square
sq1 = Square(5)
print("Perimeter = ",sq1.get_perimeter())
print("Area = ",sq1.get_area())
sq1.draw()

