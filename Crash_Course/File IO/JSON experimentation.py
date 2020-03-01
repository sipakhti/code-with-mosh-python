
import json


def to_json(filepath, obj):
    """saves the object in a file using JSON module"""

    from os import path
    import json

    overwrite = True
    # to make sure that user knows that he could overwrite existing data if present
    if path.exists(filepath):
        print(
            "the file {filepath} already exists\nproceeding will overwrtite the existing data")
        user_input = input("Press Y to continue or Press N to to stop: ")
        if user_input.lower() == "n":
            overwrite = False
        

    if overwrite:
        with open(filepath, "w") as f_obj:
            json.dump(obj, f_obj)
            print("Your file has be saved!")
            exit()
    elif overwrite:
        return None


filename = "Crash_Course/File IO/experiment_2.json"

test_list = [1, 2, 3, 4, 5, 6]
test_tuple = (15156, 468, 3543, 68746, 684, 684)
test_string = "gkuahkurhgkargknh"
test_dict = {"A": 1, "B": 2, "C": 3}

all_dict = {"test_list": test_list, "test_tuple": test_tuple, "test_string": test_string, "test_dict": test_dict}


# to_json(filename,all_dict)


with open(filename) as f_obj:
    test = json.load(f_obj)

print(test)
print(test.__len__())

# tlist = test["test_list"]
# ttuple = test["test_tuple"]
# tstring = test["test_string"]
# tdict = test["test_dict"]

# print(f"{tlist}\n{ttuple}\n{tstring}\n{tdict} ")






