import time
user_input = int(input("Enter number: "))
factors = []
prime_factors = []
is_prime = True

optimized_range = int(user_input * 0.5)

start_time = time.time_ns()
for number in range(1, optimized_range):
    if user_input % number == 0:
        factors.append(number)
end_time = time.time_ns()
loop1 = end_time - start_time

if input("Enter f to show only Factors: ").lower() == "f":
    print(*factors)


for factor in factors:
    if factor > 100:
        factor = int(factor*0.5)
    is_prime = True
    for divider in range(2, factor):
        if factor % divider == 0:
            is_prime = False
            break

    if is_prime and factor > 1:
        prime_factors.append(factor)

print(*prime_factors)
