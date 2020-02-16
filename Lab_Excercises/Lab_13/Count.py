from array import array


def count_occurances(iterable: "Iterable",element= ""):
    num_freq = {}
    for num in iterable:
        if num in num_freq:
            num_freq[num] += 1
        else:
            num_freq[num] = 1
    
    if element != "":
        return num_freq[element]


    sorted_num_freq = sorted(
        num_freq.items(), key=lambda kv: kv[1], reverse=True)
    

    return sorted_num_freq[0]


numbers = array("i")
length = int(input("enter the length of the array: "))


for x in range(length):
    verify = True
    while verify:
        verify = False
        try:
            numbers.append(int(input(f"Enter value({x+1} of {length}): ")))
        except ValueError:
            print("\033[1;31mInvalid Input, Enter only !!!INTEGERS!!!\033[0m")
            verify = True


print("most occuring value is {} with {} occurances!".format(*count_occurances(numbers)))
