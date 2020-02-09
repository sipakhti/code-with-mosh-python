
try:
    file = open("app.py")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown")
finally: # always executes whether am exception is thrown or not
    file.close()


try:
    with open("app.py") as file: # with statement automatically releases the resource
        print("file opened")
# methods with __ are reffered to as magic methods.
    # objects that support __exit__ or __enter__ (CONTEXT MANAGEMENT PROTOCOL) can be used with WITH statement
    age = int(input("Age: "))
    file.__exit__()
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown")
finally:  # always executes whether am exception is thrown or not
    file.close()


