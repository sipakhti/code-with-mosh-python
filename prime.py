from math import pow
prime = 6864797660130609714981900799081393217269435300143305409394463459185543183397656052122559640661454554977296311391480858037121987999716643812574028291115057151
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

