class Umer:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Umer(self.x + other.x, self.y + other.y)
    

point = Umer(1, 2)
other = Umer(1, 2)
combine = point + other
print(combine.x,combine.y)