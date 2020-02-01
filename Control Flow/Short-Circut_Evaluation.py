high_income = False
good_credit = True
student = True


# execution of IF statement stops when the program reachs the first FALSE value
# in case of OR the prgram stops the IF statement execution when TRUE is found 
if high_income and good_credit and not student:
    print("Eligible")