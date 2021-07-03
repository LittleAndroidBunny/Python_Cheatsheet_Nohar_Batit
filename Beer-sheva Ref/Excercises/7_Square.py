from rectangle import Rectangle
from point3 import Point


class Square(Rectangle):
    def __init__(self, *points):  # I am overriding __init__ to allow different initialization
        if len(points) == 2:  # allow the user to enter only two points!
            point1 = points[0]
            point2 = Point(points[1].x, points[0].y)
            point3 = points[1]
            point4 = Point(points[0].x, points[1].y)
            Rectangle.__init__(self, point1, point2, point3, point4)
        else:
            Rectangle.__init__(self, points)

    def calculate_area(self):
        return self.edges[0]**2

if __name__ == '__main__':
    p1 = Point(2, 3)
    p2 = Point(8, -3)
    s = Square(p1, p2)
    print(s.calculate_perimeter())
    print(s.calculate_area())


