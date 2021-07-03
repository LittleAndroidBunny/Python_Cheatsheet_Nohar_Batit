
class Point:
    """
    This class holds a point in Euclidean (2D) plane.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
            print('The point is at x: {} y: {}'.format(self.x, self.y))



if __name__ == '__main__':
    p1 = Point(2, 3)
    print(p1)
    p1.print_point()
