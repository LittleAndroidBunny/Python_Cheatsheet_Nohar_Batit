from quadrangle import Quadrangle
from point3 import Point


class Kite(Quadrangle):
    def calculate_area(self):
        p = self.points[0] - self.points[2]
        q = self.points[1] - self.points[3]
        return p*q/2


class Rectangle(Quadrangle):
    def calculate_area(self):
        return self.edges[0] * self.edges[1]

if __name__ == '__main__':
    p1 = Point(2, 3)
    p2 = Point(4, 2)
    p3 = Point(2, -2)
    p4 = Point(0, 2)
    k = Kite(p1, p2, p3, p4)
    print(k.calculate_perimeter())
    print(k.calculate_area())

    p1 = Point(2, 3)
    p2 = Point(8, 3)
    p3 = Point(8, -2)
    p4 = Point(2, -2)
    r = Rectangle(p1, p2, p3, p4)
    print(r.calculate_perimeter())
    print(r.calculate_area())


