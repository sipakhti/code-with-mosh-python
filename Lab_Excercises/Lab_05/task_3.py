name = ""
hsalary = ""
hours = ""
temp = ""
salary = 0
user_in = input(
    "Name of the Employee and their hourly wage and how many hours did they work in the last week\n")
try:
    for index in range(len(user_in)):
        if user_in[index].isnumeric():
            name = user_in[:index]
            temp = user_in[index:]
            break
    print(temp)
    temp.strip()
    for index in range(len(temp)):
        if temp[index].isspace():
            hsalary = float(temp[:index])
            hours = float(temp[index:])
            break

    if hours > 40:
        salary = (hsalary * 40) + ((hsalary * 1.5) * (hours - 40))
        print(
            f"NAME: {name.upper()}\tSALARY(regular): ${hsalary*40}\tSALARY(overtime): ${(hsalary*1.5)*(hours - 40)}\033[0m TOTAL: ${salary} ")
    else:
        salary = hsalary * hours
        print(f"NAME {name.upper()}\tSALARY: ${salary}")
except (TypeError, ValueError):
    print("You failed to enter the correct hours")
