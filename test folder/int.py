
class Length:

    __metric = {"mm": 0.001, "cm": 0.01, "m": 1, "km": 1000,
                "in": 0.0245, "ft": 0.3048, "yd": 0.9144, "mi": 1609.344}

    def __init__(self,value,unit):

        self.value = float(value)
        self.unit = unit

    @classmethod
    def from_string(cls,string):
        value, unit = string.split("-")
        return cls(value,unit)

    def convert_to_meter(self):
        meters = self.value * Length.__metric[self.unit]
        print(self.unit)

        return meters

    def __str__(self):
        return str(self.convert_to_meter()) + " m"

    def __add__(self,other):
        if type(other) == int or type(other) == float:
            val = self.convert_to_meter() + other
        else:
            val = self.convert_to_meter() + other.convert_to_meter()

        return Length(val/Length.__metric[self.unit],self.unit)

    def __lt__(self,other):
        return self.convert_to_meter() < other.convert_to_meter()

    def __le__(self,other):
        return self.convert_to_meter() <= other.convert_to_meter()

    def __eq__(self,other):
        return self.convert_to_meter() == other.convert_to_meter()

    def __ne__(self,other):
        return self.convert_to_meter() != other.convert_to_meter()

    def __ge__(self,other):
        return self.convert_to_meter() >= other.convert_to_meter()




        


a = Length(100,"m")
b = Length(1000,"cm")
print(a.convert_to_meter())
print(a+b)

print(a>b)

test = {"a":1,"b":2}
x,y=test.values()
print(x)
print(y)