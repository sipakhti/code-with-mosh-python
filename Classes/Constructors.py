class Point:
    def __init__(self, x, y):  # MAGIC METHOD called CONSTRUCTOR
        self.x = x
        self.y = y


    def draw(self):
        print(f"Point ({self.x}, {self.y})")

point = Point(1, 2)
point.z = 3
point.draw()