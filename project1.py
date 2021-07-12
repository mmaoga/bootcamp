print ()
import random

user_input = str(input("Please enter your name: ")).upper()

print ()

print(user_input, ", Welcome to the Rock, Paper, Scissors Game! Here is the winning guide for the game!! \n\n"
		+"Winning Rules of the game are as follows: \n"
		+"(1)Rock vs paper->paper wins \n"
		+"(2)Rock vs scissor->Rock wins \n"
		+"(3)Paper vs scissor->scissor wins \n\n")

user_score = 0
computer_score = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Enter your pick (rock, paper, scissors): ").lower()
    possible_actions = ["rock", "paper", "scissors"]
    while user_input not in options:
    	user_input = input("That is not a valid choice. Please try again: ").lower()
    computer_input = random.choice(possible_actions)
    print(f"\nYou picked {user_input}, computer picked {computer_input}.\n")

    if user_input == computer_input:
        print(f"Both players picked {user_input}. It's a TIE!")
    elif user_input == "rock":
        if computer_input == "scissors":
            print("You WIN!\n")
            
        else:
            print("You LOSE.\n")
            
    elif user_input == "paper":
        if computer_input == "rock":
            print("You WIN!\n")
            
        else:
            print("You LOSE.\n")
            
    elif user_input == "scissors":
        if computer_input == "paper":
            print("You WIN!\n")
            
        else:
        	print("You LOSE.\n")
        	
	  print()
	  print("You have "+str(user_wins)+" wins")
	  print("The computer has "+str(computer_wins)+" wins")
	  print()

	  repeat = input("Play again? (Y/N) ").lower()
	  while repeat not in ['y', 'n']:
	    repeat = input("That is not a valid choice. Please try again: ").lower()
	  
	  if repeat == 'n':
	    break

	  print("\n----------------------------\n")