# Greatest number finder project using conditions

a = int(input("Enter your first number: "))

b = int(input("Enter your second number: "))  # three inputs

c = int(input("Enter your third number: "))



if(a > b and a > c):
    print("The first number is the greatest number ")
elif(b > a and b > c):
    print("The second number is the greatest number")   # condition stuff
elif(c > a and c > b):
    print("The third number is the greatest number")
elif(a == b == c):
    print("All number are the same")