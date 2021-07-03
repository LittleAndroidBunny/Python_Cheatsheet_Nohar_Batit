import math
pi = math.pi

def PointsInCircum(r,n=100):
    return [point(math.cos(2 * pi / n * x) * r, math.sin(2 * pi / n * x) * r) for x in range(0, n)]

class point:
    def __init__(self, x_cord = 0.0, y_cord = 0.0):
        self.x = x_cord
        self.y = y_cord

    def __repr__(self):
        return "{x: " + str(self.x) + " y: " + str(self.y) + "}"

class circle:
    def __init__(self, center:point, radius = 1.0):
        self.center = center
        self.radius = radius

    def __repr__(self):
        return "{center: " + str(self.center) + " radius: " + str(self.radius) + "}"

    def calc_score_wrong(self, point_list)->int:
        count = 0
        for p in point_list:
            distance = ((self.center.x - p.x)**2 + (self.center.y - p.y)**2) ** 0.5
            if distance == self.radius:
                count += 1
        return count

    def calc_score(self, point_list)->int:
        epsilon = 0.000001
        count = 0
        for p in point_list:
            distance = ((self.center.x - p.x)**2 + (self.center.y - p.y)**2) ** 0.5
            if abs(distance - self.radius) <= epsilon:
                count += 1
        return count

n = 10 ** 5
prc = 100 / n
c = circle(point(0, 0), 1)
points = PointsInCircum(1, n)

print(str(c.calc_score(points) * prc) + "% of points on the circle contour")
print(str(c.calc_score_wrong(points) * prc) + "% of points on the circle contour")

