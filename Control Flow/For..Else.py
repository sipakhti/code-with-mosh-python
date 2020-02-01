successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
# FOR..else statement
else:
    print(f"Attempted {number+1} times and failed")