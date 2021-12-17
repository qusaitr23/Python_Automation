class Rectangle:
    width = 0.0
    height = 0.0

    def print_area(self):
        print(self.width * self.height)


class Circle:
    pi = 3.14
    radius = 0.0

    def print_area(self):
        print(self.pi * self.radius * self.radius)


class Triangle:
    width = 0.0
    height = 0.0

    def print_area(self):
        print((self.width * self.height) / 2)


rectangle1 = Rectangle()
rectangle1.width = 3.66
rectangle1.height = 6.17
rectangle1.print_area()


triangle1 = Triangle()
triangle1.width = 5.52
triangle1.height = 4.40
triangle1.print_area()

circle1 = Circle()
circle1.radius = 9.0
circle1.print_area()