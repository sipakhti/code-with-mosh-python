from math import pow as p
import time as t

Lap = []
test_prime = True
start = t.time_ns()
for n in range(1, 100):
    power = 2 ** n
    Fermet_P = 2 ** power + 1
    test_prime = True
    test = Fermet_P
    for num in range(1000000000000):
        test = test / 2
        if test < 2:
            test2 = True
            break
        
        test1 = int(test) + 1
        test2 = int(test) - 1
        if test2 == 1:
            test2 += 1
        
        if Fermet_P % int(test) == 0 or Fermet_P % test1 == 0 or Fermet_P % test2 == 0:
            test2 = False
            print(
                f"\033[1;31mn = {n}, number = {2 ** power + 1}, NON PRIME\033[0m ")
            test_prime = False
            break

    if test_prime:
        print(f"\033[1;32mn = {n}, PRIME = {2 ** power + 1}\033[0m ")
    
    Lap.insert(0,t.time_ns() - start)
    if n == 1:
        print(f"\033[1;33m {Lap[0]}  RATIO: 0 \033[0m ")
    else:
        print(f"\033[1;33m {Lap[0]}  RATIO: {Lap[0]//(Lap[1]+1)} \033[0m ")
    

end = t.time_ns() - start
print(end)

    
prime = 510509
test = prime

test2 = True



# for num in range(2, Fermet_P):
#         if Fermet_P % 2 == 0:
#             print(f"\033[1;31mn = {n}, number = {Fermet_P}, NON PRIME\033[0m ")
#             test_prime = False
#             break

#     if test_prime:
#         print(f"\033[1;32mn = {n}, PRIME = {Fermet_P}\033[0m ")
    
#     Lap.insert(0,t.time_ns() - start)
#     if n == 1:
#         print(f"\033[1;33m {Lap[0]}  RATIO: 0 \033[0m ")
#     else:
#         print(f"\033[1;33m {Lap[0]}  RATIO: {Lap[0]//(Lap[1]+1)} \033[0m ")
