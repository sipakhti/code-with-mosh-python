
def add(num1, num2):
    """ adds two number and returns the value"""
    return num1 + num2

def subtract(num1, num2):
    """subtracts two numbers and returns the value"""
    return num1 - num2

def divide(num1, num2):
    """ divides num1 by num2 and returns the value"""
    try:
        answer = num1 / num2
    except ZeroDivisionError:
        return "Diviser cannot be 0 !!!"
    return answer

def multiply(num1, num2):
    """multiplies num1 by num2 and returns the value"""
    return num1 * num2


# # User Input
# print("Select Operation:")
# print("1. Addition")
# print("2. Subtraction")
# print("3. Division")
# print("4. Multiplication")

# choice = input("Enter choice (1/2/3/4): ")

# num1 = int(input("Enter the first value: "))
# num2 = int(input("Enter the second value: "))

# # Understanding user input and applying the proper function
# if choice == "1":
#     print(f"{num1} + {num2} = {add(num1,num2)}")
# elif choice == "2":
#     print(f"{num1} - {num2} = {subtract(num1,num2)}")
# elif choice == "3":
#     print(f"{num1} / {num2} = {divide(num1,num2)}")
# elif choice == "4":
#     print(f"{num1} x {num2} = {multiply(num1,num2)}")

