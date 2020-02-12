# TURTLE NEED MORE REFINEMENT
def asec(*numbers):
    temp_list = []
    for num in numbers:
        for digit in num:
            temp_list.append(int(digit))
    temp_list.sort()
    print(*temp_list)


user_input = input("Enter any sequence of numbers seperated by comma(',') or by blank space")
if "," in user_input:
    tupes = user_input.split(",")
else:
    tupes = user_input.split()

asec(tupes)
