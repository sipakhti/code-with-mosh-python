# if input % 3 == 0 return Fizz
# if input % 5 == 0 return Buzz
# if input % 5 == 0 and input % 3 == 0 return FizzBuzz


def fizz_buzz(input):
    if ((input % 5 == 0) and (input % 3 == 0)):
        return "FizzBuzz"
    if (input % 5 == 0):
        return "Buzz"
    if (input % 3 == 0):
        return "Fizz"
    return input


print(fizz_buzz(9), 9)
print(fizz_buzz(20), 20)
print(fizz_buzz(15), 15)