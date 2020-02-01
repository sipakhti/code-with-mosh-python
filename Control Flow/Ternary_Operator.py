age = 22
if (age >= 18):
    message = "Eligible"
else:
    message = "Not Eligible"
print(message)


# more clearner way to do the same thing
age = 17

message = "Eligible" if age >= 18 else "Not Eligible" # ternary Operator
print(message)