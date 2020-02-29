""" Sub-Class of the Car in car module. it contains electriccar class and the supporting battery class"""

from car import Car


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles"""

    # Constructor
    def __init__(self, make, model, year, miles_per_KWh=3.4):
        """initialize attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery = Battery()
        self.range = 0
        self.miles_per_KWh = miles_per_KWh

    def get_range(self):
        """Returns the approximate range of the car based on the
        amount of charge the battery has"""

    # range is calculated by a static value of miles_per_KWh which is then multiplied by the
    # the fraction of the battery charge
        self.range = self.battery.battery_size * \
            self.miles_per_KWh * (self.battery.battery_charge / 100)

        return int(self.range)

    # Alternate Constructor
    @classmethod
    def from_string(cls, electiccar_string, seperator="-"):
        make, model, year, mpKWh = electiccar_string.split(seperator)

        return cls(make, model, int(year), int(mpKWh))


# Inheritance

class Battery():
    """support class of ElectricCar class which has code
    for battery related things"""

    battery_capacity_unit = "KWh"

    def __init__(self, battery_size=70, battery_charge=100):
        self.battery_size = battery_size
        self.battery_charge = battery_charge

    def describe_battery(self):
        print(
            f"This car has a {self.battery_size}-{ElectricCar.battery_capacity_unit} battery ")

    # 9.9
    # upgrades battery capacity to user input or the default value of 85
    def battery_upgrade(self, bat_size=85):
        if self.battery_size == bat_size:
            return f"Already upgraded to {bat_size}!"
        elif self.battery_size < 85:
            self.battery_size = bat_size
