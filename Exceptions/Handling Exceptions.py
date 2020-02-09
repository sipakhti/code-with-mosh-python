try: 
    age = int(input("Age: "))
    xfactor = 10 / age
except ValueError as error:
    print("You didn't enter a valid age.")
except ZeroDivisionError:
    print("age cannot be zero")
else:
    print("No exceptions were thrown")
print("execution contiunes")


try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown")

