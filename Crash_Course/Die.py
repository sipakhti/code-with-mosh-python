from random import randint, seed
from time import time_ns

class Die():
    """creates a dice with inputed sides (default=6)"""

    # Constructor
    def __init__(self, sides=6):
        self.sides = sides
    
    # rolls the dice 
    def roll_die(self, n=1):
        """ prints random dice value"""
        for i in range(n):
            seed(i)
            print(randint(1,self.sides))

test = Die(20)
test.roll_die(10)


