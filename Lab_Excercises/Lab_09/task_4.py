user_input = int(input("Enter value of n: "))

# LEFT STAR ARROW
for number in range(user_input):
    print(f"{' '*(user_input-number)}{'*'*(user_input-number)} ")

for number in range(2,user_input+1):
    print(f"{' '*(number)}{'*'*(number)} ")

# RIGHT STAR ARROW
for number in range(user_input):
    print(f"{'  '*(number)}{'*'*(user_input-number)} ")

for number in range(2,user_input+1):
    print(f"{'  '*(user_input-(number))}{'*'*(number)} ")