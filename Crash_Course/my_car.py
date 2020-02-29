
from electric_car import ElectricCar
from car import Car
import assorted as A


my_new_car = Car("Audi", "A6", 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()


tesla = ElectricCar("Tesla", "model X", 2019)
print(tesla.get_descriptive_name())
print(
    f"This car can go approximately {tesla.get_range()} miles on a single charge")

tesla.battery.battery_upgrade()
print(
    f"This car can go approximately {tesla.get_range()} miles on a single charge")
