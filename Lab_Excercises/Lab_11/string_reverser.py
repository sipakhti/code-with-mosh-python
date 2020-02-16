import time as t


def str_reverse(string: str = ...):
    temp_list = []
    for char in string:
        temp_list.append(char)

    return list_concat(temp_list)


def list_concat(items: str):
    """ concatenate list elements"""
    out = ""
    for element in items:
        out = out + element
    return out


# MAIN
user_input = input("Enter a String: \n")

while user_input.lower() != "q":


    print(str_reverse(user_input))



    user_input = input(
        "Enter 'q' to quit else enter any string to reverse: \n")
