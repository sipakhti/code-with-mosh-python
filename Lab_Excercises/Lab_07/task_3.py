import time
from array import array

prime = 6700417
temp = True

temp_list = list(range(2, prime))
temp_array = array("I", temp_list)

for_start = time.time_ns()

# NORMAL FOR LOOP
for number in temp_list:
    if prime % number == 0:
        print(f"{prime} is not a prime number")
        temp = False
        break
for_end = time.time_ns()

for1_total = for_end - for_start

# ARRAY FOR LOOP
for_start = time.time_ns()
for number in temp_array:
    if prime % number == 0:
        print(f"{prime} is not a prime number")
        temp = False
        break
for_end = time.time_ns()

array_total = for_end - for_start


if temp:
    print("PRIME")
# OPTIMIZED FOR LOOP FOR PRIME IDENTIFICATION
opt_prime = int(prime*0.5)+1
for_start = time.time_ns()
for number in range(2, opt_prime):
    if prime % number == 0:
        print(f"{prime} is not a prime number")
        temp = False
        break
for_end = time.time_ns()
for2_total = for_end - for_start


prime = 6700417
temp = True
count = 2

# NORMAL WHILE LOOP
while_start = time.time_ns()
while count < prime:

    if prime % count == 0:
        print(f"{prime} is not a prime number")
        temp = False
        break

    count += 1

while_end = time.time_ns()
while_total = while_end - while_start

if temp:
    print("PRIME")

print(f"FOR: {for1_total}   WHILE: {while_total}")
print(f"normal FOR loop: {for1_total}", f"optimzed FOR loop: {for2_total}",
      f"speed factor: {for1_total / for2_total}")
print(f"normal FOR loop: {for1_total}", f"normal WHILE loop: {while_total}",
      f"speed factor: {for1_total / while_total}")
print(f"speed factor: {while_total/for2_total} (WHILE / optimized FOR)")
print(f"array loop: {array_total} speed factor: {for1_total/array_total} ")

# print(timeit(case1,number=1),timeit(case2,number=1))
with open("output.txt", "w") as file:
    file.write(
        f"normal FOR loop: {for1_total} optimzed FOR loop: {for2_total} speed factor: {for1_total / for2_total}")
    file.write(
        f"normal FOR loop: {for1_total} normal WHILE loop: {while_total} speed factor: {for1_total / while_total}")
    file.write(
        f"speed factor: {while_total/for2_total} (WHILE / optimized FOR)")
