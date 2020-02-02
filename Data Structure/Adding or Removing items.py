letters = list("abc")


# Add
letters.append("d")  # at the end of the list
letters.insert(0, "-")  # at the index required


#remove
letters.pop()  # by default removes the last item in the list. Also removes the value at the specified index
letters.remove("b")  # remove the first occurance of the matching value. need to loop the list if more than one occurance
del letters[0:3]  # can delete the specified index or a whole range of values 
letters.clear()  # removes all items from the list