
class Car():
    """ Simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """ attribute initialization"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
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

my_new_car = Car("Audi", "A6", 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()


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
        

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles"""


    def __init__(self, make, model, year, miles_per_KWh=3.4):
        """initialize attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery = Battery()
        self.range = 0
        self.miles_per_KWh = miles_per_KWh
    
    def get_range(self):
        """Returns the approximate range of the car based on the
        amount of charge the battery has"""

        self.range = self.battery.battery_size * self.miles_per_KWh * (self.battery.battery_charge / 100)
        
        return int(self.range)

        

tesla = ElectricCar("Tesla", "model X", 2019)
tesla.battery.battery_size = 145
tesla.battery.battery_charge = 87
print(tesla.get_descriptive_name())
print(f"This car can go approximately {tesla.get_range()} miles on a single charge")
