
from assorted import str_to_int_list

class MathOperators():
    """ contains methods to add, subtract, divide or multiply"""
    

    # CONSTRUCTOR
    def __init__(self, *numbers):
        self.numbers = numbers

    # Alternate Constructor
    @classmethod
    def from_string(cls, user_string, seperator=" "):
        """takes a string on integers and parse it into a list of integers
            based on the seperator used. The Default seperator is a space(' ')
        """
        parsed_string = str_to_int_list(user_string, seperator)
        return cls(*parsed_string)

    def add(self):
        """ adds given numbers and returns the value"""
        answer = 0
        for number in self.numbers:
            answer += number

        return answer

    def subtract(self):
        """subtracts given numbers and returns the value"""
        answer = 0
        for number in self.numbers:
            answer -= number

        return answer

    def divide(self):
        """ divides num1 by num2 and returns the value"""

        try:
            num1, num2 = self.numbers
            answer = num1 / num2
        except ZeroDivisionError:
            return "Diviser cannot be 0 !!!"
        except ValueError:
            return "input numbers cannot be more than 2!!!"
        return answer

    def multiply(self):
        """multiplies all the numbers and returns the value"""
        answer = 0
        for number in self.numbers:
            answer *= number
        return answer
