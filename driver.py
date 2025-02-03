import rpsLogic

print("Welcome to the game of Rock, Paper, Scissors")

print("Here are the instructions below: ")
print("Please type in whether you are going for rock, paper or scissors. r = rock, p = paper and s = scissors")
print("You can also type in any letter to quit the game at any time.") 
print("The game will keep going until you decide to quit.")

doit = True

while doit:
    #create a user input
    user_input = input("Enter your choice (r, p, s): ")

    #check if user wants to quit and make rpsObject
    if user_input == 'r' or user_input == 'p' or user_input == 's':
       userObject = rpsLogic.rpsMake(user_input)

       #get the computer's choice
       computerObject = rpsLogic.randomChoice()

       print(f"{userObject.name} vs. {computerObject.name}")
       result = rpsLogic.testWin(computerObject, userObject)
       if result == 1:
           print("You win!")
       elif result == 2:
           print("You lose!")   
       else:
            print("It's a tie!")

    else:
       print("Thanks for playing!")
       doit = False




    



