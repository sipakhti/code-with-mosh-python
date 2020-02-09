from timeit import timeit



code = """

def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age
    
try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

code1 = """

def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age
    

xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass

"""
code_0 = timeit(code, number=10000000)
code_1 = timeit(code1, number=10000000)
print("first code",code_0 )

print("second code",code_1)

print(code_0/code_1)
