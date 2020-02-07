numbers = dict(first=0, second=0, third=0, fourth=0)
liss = []
for key in numbers:
    numbers[key] = float(input(f"Enter {key} number: "))
    liss.append(numbers[key])

sorted_numbers = [b for a, b in (
    sorted(numbers.items(), key=lambda kv: kv[1]))]

print(
    f"The largest of {liss[0]}, {liss[1]}, {liss[2]} and {liss[3]} is {sorted_numbers[-1]}")
