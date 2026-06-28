# Marks data storer using dictionary in python

result = {} # empty dictionary
   
   
   
chem = int(input("Enter your chemistry marks: "))
physics = int(input("Enter your physics marks: ")) # data stored in variable
maths = int(input("Enter your maths marks: "))

result.update({"Chemistry" : chem})
result.update({"Physics" : physics}) # adding the data to empty dictionary using update function
result.update({"Maths" : maths})



print(result)