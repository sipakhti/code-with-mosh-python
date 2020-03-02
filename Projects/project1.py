
from assorted import str_to_int_list

class MathOperators():
    """ contains methods to add, subtract, divide or multiply"""

    # CONSTRUCTOR
    def __init__(self, *numbers):
        self.numbers = numbers

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

    def divide(self,num1, num2):
        """ divides num1 by num2 and returns the value"""
        try:
            answer = num1 / num2
        except ZeroDivisionError:
            return "Diviser cannot be 0 !!!"
        return answer

    def multiply(self):
        """multiplies all the numbers and returns the value"""
        answer = 0
        for number in self.numbers:
            answer *= number
        return answer







error = True



while True:

    # User Input
    print("Select Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    print("!!!ENTER q to QUIT!!!")

    choice = input("Enter choice (1/2/3/4) or 'q': ")

# Makes sure that entered value is within parameters
    while not (choice in "1234" or choice.lower() == 'q'):
        print("Enter the correct option!")
        choice = input("Enter choice (1/2/3/4) or 'q': ")

# in case a wrong value is entered
    # while error:
    #     try:
    #         num1 = int(input("Enter the first value: "))
    #         num2 = int(input("Enter the second value: "))
    #     except ValueError:
    #         print("\033[31m!!!Wrong Input!!!\033[0m")
    #     else:
    #         error = False

# instantiating MathOperators class
    answer = MathOperators(num1, num2)


# Understanding user input and applying the proper function
    if choice.lower() == "q":
        print("The Program is quiting.")
        break


# ADDITION
    if choice == "1":
        print("To calculate sum of multilpe numbers enter the numbers seperated by a space.")
        try:
            user_in = input("otherwise press enter to continue.")
        except ValueError:
            print(f"\033[32m{num1} + {num2} = {answer.add()}\033[0m")
        else:
            answer.numbers = str_to_int_list(user_in)
            print("\033[32m",end="") # to colorize the output
            print(*answer.numbers,sep="+",end=f" = {answer.add()}\n\033[0m")
# SUBTRACTION        
    elif choice == "2":
        print(
            "To calculate sum of multilpe numbers enter the numbers seperated by a space.")
        try:
            user_in = input("otherwise press enter to continue.")
        except ValueError:
            print(f"\033[32m{num1} + {num2} = {answer.subtract()}\033[0m")
        else:
            answer.numbers = str_to_int_list(user_in)
            print("\033[32m", end="")  # to colorize the output
            print(*answer.numbers, sep="-", end=f" = {answer.subtract()}\n\033[0m")
# DIVISION
    elif choice == "3":
        print(f"\033[32m{num1} / {num2} = {answer.divide(num1,num2)}\033[0m")
# MULTIPLICATION
    elif choice == "4":
        print(
            "To calculate product of multilpe numbers enter the numbers seperated by a space.")
        try:
            user_in = input("otherwise press enter to continue.")
        except ValueError:
            print(f"\033[32m{num1} + {num2} = {answer.multiply()}\033[0m")
        else:
            answer.numbers = str_to_int_list(user_in)
            print("\033[31m", end="")  # to colorize the output
            print(*answer.numbers, sep="x", end=f" = {answer.multiply()}\n\033[0m")
