message = "a"

def greet(name):
    global message  # exteremly bad practice
    message = "b"

greet("Umer")
print(message)