import random

options = ['rock', 'paper', 'scissors']
user_score = 0
computer_score = 0

def pick_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("draw")
        return 0,0
    #user_choice wins
    if (user_choice == "rock" and computer_choice == "scissors" or user_choice =="paper" and computer_choice == "rock"
            or user_choice == "scissors" and computer_choice == "paper"):
        print(f"{user_choice} beats {computer_choice}-User wins!")
        return 1, 0
    #computer_choice wins
    elif (computer_choice == "rock" and user_choice == "scissors" or computer_choice =="paper" and user_choice == "rock"
            or computer_choice == "scissors" and user_choice == "paper"):
        print(f"{computer_choice} beats {user_choice}-Computer wins!")
        return 0, 1
#function to check user input
def get_user_choice():
    while True:
        user_choice = input("Rock, Paper, or Scissors?: ").lower()
        if user_choice in options:
            return user_choice
        else:
            print(f"Invalid choice - Please choose one of: {', '.join(options).capitalize()}")
game_on = True
while game_on:
    print(f"User: {user_score} Computer: {computer_score}")
    user_pick = get_user_choice()
    choice_2 = random.choice(options).lower()
    user_change, computer_change = pick_winner(user_pick, choice_2)
    user_score += user_change
    computer_score += computer_change
    if input("Play again?: Yes or No: ").lower() == "no":
        game_on = False
        print(f"User Score {user_score}, Computer Score {computer_score}")
        if user_score > computer_score:
            print("User Wins!")
        else:
            print("Computer Wins!")