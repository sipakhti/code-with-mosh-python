# PART A
#  first n odd numbers and their sum.
print("PART A: nth odd numbers and their sum")
nth_number = int(input("Enter a number:\n"))
temp = True
prime_sum = 0
for digit in range(2, nth_number + 1):
    temp = True
    for is_prime in range(2, digit):
        if digit % is_prime == 0:
            temp = False
            break
    if temp:
        prime_sum += digit
        print(digit, prime_sum)

# PART B
input("Press any key to check for PERFECT NUMBER!\n")

user_input = int(input("Enter any Intger:\n"))
divisors = []

for number in range(1, user_input):
    if user_input % number == 0:
        divisors.append(number)

if sum(divisors) == user_input:
    print(f"{user_input} is a Perfect Number!")
else:
    print(f"{user_input} is not a Perfect Number!")
