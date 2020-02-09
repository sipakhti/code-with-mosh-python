import time
prime = 6700417 # int(input("Enter any number to check prime: "))
temp = True
#case1 = """
prime = 6700417
temp = True
for_start = time.time_ns()
for number in range(2, prime):
    if prime % number == 0:
        print(f"{prime} is not a prime number")
        temp = False
        break
for_end = time.time_ns()
for_total = for_end - for_start

if temp:
    print("PRIME")


#case2 ="""
prime = 6700417
temp = True
count = 2
count1 = prime//10
while_start = time.time_ns()
while count < prime:
    
    
    if prime % count1 == 0:
        print(f"{prime} is not a prime number")
        temp = False
        break
    count1 -= 1
    

    if prime % count == 0:
        print(f"{prime} is not a prime number")
        temp = False
        break

    if count1 < count:
        break
    count += 1
while_end = time.time_ns()
while_total = while_end - while_start

if temp:
    print("PRIME")

print(f"FOR: {for_total}   WHILE: {while_total}")

#print(timeit(case1,number=1),timeit(case2,number=1))