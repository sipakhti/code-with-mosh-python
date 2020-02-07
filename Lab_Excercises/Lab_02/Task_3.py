num_odd = int(input("How many first odd numbers do you want to Square? "))
for odd in range(1, num_odd*2, 2):
    print(f"Square of {odd} = {odd*odd}")