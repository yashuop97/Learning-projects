# School database system using OOPS 

class school: 

    classes = 10
    teachers = 20   # these values are same for every student
    student = 100
    principal = 1


    def __init__(self, student, std, marks): # using __init__ dunder function to store the data of student
        self.student = student
        self.std = std      # storing the data in variable
        self.marks = marks
        
    

student1 = school("Yash", "1st", 0) # first student data storing in the class

print(student1.student)
print(student1.marks)
print("The first student name and marks")  


student2 = school("Justin", "10th", 99) # second student data

print(student2.student)
print(student2.marks)
print("The second student name and marks")



if(student1.marks >= 80):
    print("\n",student1.student, "PASSED the exam")
else:
    print("\n",student1.student, "FAILED the exam")         # this tells if the student passed or not

if(student2.marks >= 80):
    print("\n",student2.student, "PASSED the exam")
else:
    print("\n",student2.student, "FAILED the exam")


# thats it!