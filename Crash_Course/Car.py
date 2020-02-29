
"""Module which contains the Class Car that represents a car"""


class Car():
    """ Simple attempt to represent a car"""

    # Constructor
    def __init__(self, make, model, year):
        """ attribute initialization"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    # Alternate Constructor
    @classmethod
    def from_string(cls, car_string, seperator="-"):
        make, model, year = car_string.split(seperator)

        return cls(make, model, int(year))

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"

        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """ sets the odometer value and makes sure that 
        it cant be lowered back"""

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")



