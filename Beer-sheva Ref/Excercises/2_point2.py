
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
            print('The point is at x: {} y: {}'.format(self.x, self.y))

    def __repr__(self):
        return 'The point is at x: {} y: {}'.format(self.x, self.y)


if __name__ == '__main__':
    p1 = Point(2, 3)
    p1.print_point()
    print(p1)

