import json

filename = "Crash_Course/File IO/username.json"

try:
    with open(filename) as file_object:
        username = json.load(file_object)
        print(f"Welcome back {username}")
except FileNotFoundError:

    username = input("Please enter your name: ")
    with open(filename, "w") as file_object:
        json.dump(username, file_object)
        print(f"I will remmember the next time you'll be here {username}.Ciao! ")


