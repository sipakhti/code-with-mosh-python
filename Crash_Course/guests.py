
import time as t
user_name = input("Enter your name: ")
guests_file = "guests.txt"

with open(guests_file) as file_object:
    names = file_object.readlines()

print(*names)
# with open(guests_file, "a") as file_object:
#     file_object.write(f"{user_name}\n")


print(t.strftime("%d/%m/%Y %H:%M:%S"))


while True:

    user_name = input("Enter your name or to quit enter 'q':")
    if user_name.lower() == "q":
        break
    with open("guest_book.txt", "a") as file_object:
        file_object.write(f"{user_name}\t{t.strftime(' %d/%m/%Y %H:%M:%S')}\n")


with open("guest_book.txt") as file_object:
    lis = file_object.readlines()

print(*lis)
