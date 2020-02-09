month_name = {1: "January", 2: "Feburary", 3: "March", 4: "April", 5: "May",
              6: "June", 7: "July", 8: "August", 9: "September", 10: "October",
              11: "November", 12: "December"}


date = int(
    input("Enter date in the following format \033[1;31m DDMMYYYY\033[1;32m\033[1B\033[8D"))
print("\033[97m")

day = date // 1000000
month = (date // 10000) % 100
year = date % 10000


while ((day > 31 or day < 0) or (month > 12 or month < 0) or (len(str(date)) != 8)):
    print("Wrong date format")
    date = int(
        input("Enter date in the following format \033[1;31m DDMMYYYY:"))
    print("\033[97m")
    day = date // 1000000
    month = (date // 10000) % 100
    year = date % 10000


print(f"{day} {month_name[month]} {year}")
