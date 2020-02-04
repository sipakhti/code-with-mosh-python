

numbers = [1, 1, 2, 3, 4, 5, 5, 6]
first = set(numbers)
second = {1, 10}

# Union of two sets(values from both sets)(full join{without duplicates})
print(first | second)
# Intersection of two sets (values in both first and second sets)(inner join)
print(first & second)
# Difference of two sets (Values which are present in one set but not the other)(left join where <column_name> = NULL)
print(first - second)
# Sematric Difference (values in either the first or the second set but not both)
print(first ^ second)

# SETS are unordered collections so no indexing options unlike lists
# print(first[0])  # doesn't work and gives a runtime error
