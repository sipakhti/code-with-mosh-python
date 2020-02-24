class Point:
    def draw(self):
        print("DRAW")

point = Point()
print(type(point))
print(isinstance(point,Point))
point.draw()