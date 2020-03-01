
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
        return "Division by 0 is not Valid!!!"
    return answer

def multiply(num1, num2):
    """multiplies num1 by num2 and returns the value"""
    return num1 * num2


