from name_function import formatted_name

print("Enter 'q' at anytime to quit the program!")
while True:
    first_name = input("Please give me a first name: ")
    if first_name.lower() == "q":
        break
    last_name = input("Please give me a last name: ")
    if last_name.lower() == "q":
        break

    print(f"Neatly Formatted Name: {formatted_name(first_name,last_name)}")


