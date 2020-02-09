from math import pow
nth_term = int(input("Input the value of the nth term: "))
series_sum = 0
for x in range(1, nth_term + 1):
    print(f"1/{x}^{x} =", 1 / (pow(x, x)))
    series_sum += 1 / (pow(x, x))

print("The sum of the above series is:", series_sum)
