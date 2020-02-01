# AND Operator T,T
high_income = True
good_credit = True

if (high_income and good_credit):
    print("Eligible")
else:
    print("Not Eligible")
# AND Operator F,T
high_income = False
good_credit = True

if (high_income and good_credit):
    print("Eligible")
else:
    print("Not Eligible")

# OR Operator T,T
high_income = True
good_credit = True

if (high_income and good_credit):
    print("Eligible")
else:
    print("Not Eligible")


# OR Operator F,T
high_income = True
good_credit = True

if (high_income and good_credit):
    print("Eligible")
else:
    print("Not Eligible")


# Not Operator 
high_income = True
good_credit = True
student = True

if (not student):
    print("Eligible")
else:
    print("Not Eligible")


# OR Operator T,T
high_income = True
good_credit = True
student = False

if ((high_income and good_credit)):
    print("Eligible")
else:
    print("Not Eligible")
