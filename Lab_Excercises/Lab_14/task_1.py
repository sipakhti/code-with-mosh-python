def print_column(list1: "iterable", list2=[], col1="column 1", col2="column 2", dupes: bool = False):
    """ Outputs iterable in a verticle fashion.
        if a second list is provided with matching length and having a relationship
        between the corresponding values of both lists
        the function creates a second column to display them side by side
        if you want to get the length of individual elements then change dupes=True
        in case of dupes=True then the second argument will not give any results
    """
#    if dupes:
#        list2 = seq_count(list1)

    if bool(list2):
        print(
            f"{col1}{' '*(len(col1)+len(max(list1)))}{' '*( len(max(list1)))}{col2}\n")
        for x in range(len(list1)):
            print(
                f"{list1[x]}{' '*(len(col1)+len(max(list1)))}{' '*( len(max(list1)) - len(list1[x])  + len(max(list1)))}{list2[x]} ")
    else:
        print(f"{col1}{' '*3}{' '*len(max(list1))}INDEX\n")
        for x in range(len(list1)):
            print(
                f"{list1[x]} {'>'*5}{' '*(( len(max(list1))-len(list1[x]) ) + len(max(list1)))}{x} ")


def hi_temp(iterable: "of type int"):
    """ Takes a 2D list or array and returns a list containing
        the highest value in a row cooresponding to the row index
    """

    cities_max_temp = []
    max_temp = 0
    for row in iterable:
        for temprature in row:
            if temprature.isnumeric():
                if int(temprature) > max_temp:
                    max_temp = int(temprature)
        cities_max_temp.append(max_temp)
        max_temp = 0

    return cities_max_temp


num_cities = int(
    input("Enter the number of cities you want to add the data of: "))

print("Enter the city name followed by temprature in C, everything must be seperated by ','(comma)\n")
print("CITY,TEMPRATURE... The week starts from Sunday")

temp_list = [[row_val for row_val in input(
    f"City {i+1}\n").split(",")] for i in range(num_cities)]

temp_list.insert(0, ["City", "Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"])

cities = []
for row in temp_list:
    cities.append(row[0])

for row in temp_list:
    for element in row:
        if element.isalpha() and len(element) > 2:
            print(
                f"{element}  ", end=f"{' '*(len(max(cities,key= lambda c:len(c)))-len(row[0]))}")
        else:
            print(f"{element.zfill(2)}", end="  ")
    print("")

print_column(cities, hi_temp(temp_list), col1="CITY", col2="TEMP(C)")
