import time as t


def str_reverse(string: str = ...):
    temp_list = []
    for char in string:
        temp_list.append(char)

    return list_concat(temp_list)


def list_concat(*items: str):
    out = ""
    for index in range(len(items[0])):
        out = out + items[0][len(items[0])-index-1]
    return out


# MAIN
user_input = input("Enter a String: \n")

while user_input.lower() != "q":

    start = t.time_ns()
    print(str_reverse(user_input))
    end = t.time_ns()
    custom_func = end - start

    start = t.time_ns()
    print(user_input[::-1])
    end = t.time_ns()
    indexing = end - start
    print(
        f"custom function: {custom_func} indexing: {indexing} ratio: {indexing/custom_func} ")
    user_input = input(
        "Enter 'q' to quit else enter any string to reverse: \n")
