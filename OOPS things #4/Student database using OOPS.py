# using OOPS class and init dunder function and using self

class student:


    def __init__(self, name, marks, age):  # __init__ is a dunder function most useful dunder function actually
        self.name = name  
        self.marks = marks # storing the value in variable
        self.age = age 



s1 = student("Yash", 33, 0)  # storing the data in class
print(s1.name)


s2 = student("Alex", 92, 17) # same thing
print(s2.name)     
