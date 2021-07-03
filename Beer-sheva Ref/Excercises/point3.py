
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
            print('The point is at x: {} y: {}'.format(self.x, self.y))

    def __repr__(self):
        return 'The point is at x: {} y: {}'.format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

if __name__ == '__main__':
    p1 = Point(2, 3)
    p2 = Point(5, -1)
    p3 = p1 + p2
    print(p3)
    distance = p1 - p2
    print(distance)
