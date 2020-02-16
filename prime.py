from math import pow
prime = 510509
test = prime

test2 = True
for num in range(1000000000000):
    test = test / 2
    if test < 2:
        test2 = True
        
        break
    if  prime % int(test) == 0 or prime % (int(test)+1) == 0 or prime % (int(test)-1) == 0:
        test2 = False
        print("not prime",test,num)
        break

if test2:
    print("prime")

for num in range(2,211):

    print("BOOO yaaa")
    print(211/num)