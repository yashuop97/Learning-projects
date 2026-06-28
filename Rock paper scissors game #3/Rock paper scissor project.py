import random # using import module to create random computer choices

Choice = input("Choose Rock, Paper, or Scissors: ").capitalize() # user choice we capatilize so user can type "rock" no need for "Rock"



choices = ["Rock", "Paper", "Scissors"] # all choices
ComputerChoice = random.choice(choices) # computer choose a random option from choices



print(f"Computer Chose: {ComputerChoice}")
print(f"You chose: {Choice}")



if Choice == ComputerChoice:
    print("Its a tie!")
elif (Choice == "Rock" and ComputerChoice == "Scissors"):
     print("You Won!")
elif (Choice == "Paper" and ComputerChoice == "Rock"):    # conditions to tell if the user won or the computer 
     print("You Won!")
elif (Choice == "Scissors" and ComputerChoice == "Paper"):
     print("You Won!")


else:
    print("You Lost!")  # else is used for all the possibility in which the user lost