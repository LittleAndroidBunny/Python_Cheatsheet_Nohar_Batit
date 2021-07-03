from math import acos
from point3 import Point


class Quadrangle:
    """
    This class holds a quadrangle in Euclidean plane.
    """
    def __init__(self, *points):
        self.points = []
        self.edges = [-1,-1,-1,-1]
        self.angels = [-1,-1,-1,-1]
        for point in points:
            self.points.append(point)
        self.calculate_edges_from_points()
        self.calculate_angels_from_points()

    def __iter__(self):
        # this will make the class as iterator
        self.i = -1
        return self

    def __next__(self):
        # this will send the next point
        self.i = self.i+1
        if self.i == 4:
            raise StopIteration
        return self.points[self.i]

    def calculate_edges_from_points(self):
        self.edges[0] = self.points[0] - self.points[1]
        self.edges[1] = self.points[1] - self.points[2]
        self.edges[2] = self.points[2] - self.points[3]
        self.edges[3] = self.points[3] - self.points[0]

    def calculate_angels_from_points(self):
        """
        using the Law of cosines
        :return:
        """
        for i in range(4):
            c = (self.points[i - 1] - self.points[(i + 1) % 4])
            a = (self.points[i] - self.points[(i + 1) % 4])
            b = (self.points[i - 1] - self.points[i])
            d = (c**2 - a**2 - b**2) / (2*a*b)
            self.angels[i] = acos(d)

    def calculate_area(self):
        # TODO
        pass

    def calculate_perimeter(self):
        return sum(self.edges)

if __name__ == '__main__':
    p1 = Point(2, 3)
    p2 = Point(4, 2)
    p3 = Point(3, -2)
    p4 = Point(1, 1)
    q = Quadrangle(p1, p2, p3, p4)
    print(q.calculate_perimeter())
    print('************************************')
    for point in q.points:
        print(point)
    print('************************************')
    for point in q:
        print(point)
    print('************************************')
    q_iter = iter(q)
    for i in range(4):
        print(next(q_iter))


