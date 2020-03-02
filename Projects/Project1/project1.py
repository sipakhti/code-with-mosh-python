
from mathoperatorss import MathOperators

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


# EXIT case
    if choice.lower() == "q":
        print("The Program is quiting.")
        break


# ADDITION
    if choice == "1":
        print(
            "To calculate sum of multilpe numbers enter the numbers seperated by a space.")
        user_in = input()
        answer = MathOperators.from_string(user_in)
        print("\033[32m", end="")  # to colorize the output
        print(*answer.numbers, sep="+", end=f" = {answer.add()}\n\033[0m")

# SUBTRACTION
    elif choice == "2":
        print(
            "To calculate sum of multilpe numbers enter the numbers seperated by a space.")
        user_in = input()
        answer = MathOperators.from_string(user_in)
        print("\033[32m", end="")  # to colorize the output
        print(*answer.numbers, sep="-", end=f" = {answer.subtract()}\n\033[0m")

# DIVISION
    elif choice == "3":
        user_in = input("Enter two numbers seperated by a blank: ")

        answer = MathOperators.from_string(user_in)
        print("\033[32m", end="")  # to colorize the output
        print(*answer.numbers, sep="/", end=f" = {answer.divide()}\n\033[0m")
# MULTIPLICATION
    elif choice == "4":
        print(
            "To calculate product of multilpe numbers enter the numbers seperated by a space.")
        user_in = input()
        answer = MathOperators.from_string(user_in)
        print("\033[31m", end="")  # to colorize the output
        print(*answer.numbers, sep="x", end=f" = {answer.multiply()}\n\033[0m")
