def greet(name):
    print(f"Hi {name}")


# Types
# 1- Perform a task eg.greet()
# 2- Return a Value eg round()


def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Umer")
print(message)
file = open("Content.txt", "w")
file.write(message)
file.close()