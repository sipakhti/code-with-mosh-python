# 9.1 page 


class Restaurant():
    """ class to decribe a restraunt and open or close it"""

    def __init__(self, restraunt_name, cuisine_type):
        self.restraunt_name = restraunt_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # 9.4

    def describe_restraunt(self):
        print(
            f"The Restraunt is names '{self.restraunt_name.title()}' and offers {self.cuisine_type.title()} Cuisine.")

    def open_restraunt(self):
        print(f"The {self.restraunt_name.title()} is now OPEN!")

    def close_restraunt(self):
        print(f"The {self.restraunt_name.title()} is now CLOSE!")

#9.4
    def set_number_served(self, customers):
        """Sets the Value of number os customers served"""
        self.number_served = customers
    
    def increment_number_served(self, customers):
        """Adds the given amount to the number of customers served"""
        self.number_served += customers


    @classmethod
    def from_string(cls, restraunt_string, seperator):
        restraunt_name, cuisine_type = restraunt_string.split(seperator)
        return cls(restraunt_name, cuisine_type)


# restraunt = Restaurant("Tenerife", "Italian")
# print(restraunt.restraunt_name)
# print(restraunt.cuisine_type)
# restraunt.open_restraunt()
# restraunt.close_restraunt()

# restraunt_string_in = input("Enter the name of the restraunt: ")
# seperator = input("Enter the seperator used to seperate different fields: ")

# restraunt_2 = Restaurant.from_string(restraunt_string_in, seperator)

# print(restraunt_2.restraunt_name)
# print(restraunt_2.cuisine_type)
# restraunt_2.open_restraunt()
# restraunt_2.close_restraunt()


# 9.2

restraunt = Restaurant("Tenerife", "Italian")
restraunt_2 = Restaurant("shahbaz tikka", "Pakistani")
restraunt_3 = Restaurant("bistro 101", "oriental")

restraunt.describe_restraunt()
restraunt_2.describe_restraunt()
restraunt_3.describe_restraunt()

# 9.6 Icecream stand (INHERITANCE)

class IceCreamStand(Restaurant):
    """ Sub class of Restraunt which deals with specifically
    IceCreamStands"""

    def __init__(self, restraunt_name, cuisine_type):
        super().__init__(restraunt_name, cuisine_type)
        self.flavours = []


    def set_flavours(self, flavours: "Provide a list"):
        """ Sets the flavours attribute with the user provided list"""
        self.flavours = flavours
    

    def flavour_from_string(self, flavours_string, seperator):
        """ string parser for the flavour attribute"""
        self.flavours = list(flavours_string.split(seperator))

    def print_flavours(self):
        """prints the complete falvour list on the console"""
        print(*self.flavours)
