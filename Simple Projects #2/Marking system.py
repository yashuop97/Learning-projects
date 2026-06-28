# Grading system using condition python


percentage = float(input("Enter you percentage: ")) # input


if(percentage >= 90.0):
    print("Your grade is A, Congratulations your hard work paid off!!")
elif(percentage < 90.0 and percentage >= 80):
    print("Your grade is B, You can improve keep working hard!!")
elif(percentage < 80 and percentage >= 70):
    print("Your grade is C, You need to improve take tuitions!!")     # conditions to get to tell the grade based on percentage
elif(percentage < 70 and percentage >= 50):
    print("Your grade is D, Very poor performance this is not acceptable")
elif(percentage < 50 and percentage > 0):
    print("Your grade is F, You failed the class come meet me at the office")
else:
    print("You didnt even gave the exam, You failed!!")


print("\nThanks for using our service")  # proffesional stuff hehe

