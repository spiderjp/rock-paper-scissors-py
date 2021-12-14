import random

while True:

    user_action = input("Enter a choice: rock, paper or scissors:")
    possible_actions = ['Rock', "Paper", "Scissors"]
    computer_action = random.choice(possible_actions)

    print(f"\nYou chose {user_action}, I chose {computer_action}. \n")

    if user_action.lower() == computer_action.lower():

        print(f"Both players selected {user_action}. It's a tie!")

    elif user_action == "rock" and computer_action.lower() == "scissors":

        print("Rock smashes scissors! You win!")


    elif user_action.lower() == "paper" and computer_action.lower() == "rock":

        print("Papers covers rock! You win!")

    elif user_action.lower() == "scissors" and computer_action.lower() == "paper":

        print("Scissors cuts paper! You win!")

    else:

        print("I Win!")


    play_again = input("Play again? (Y)es/(N)o:")
    if play_again.lower() != "y":

        break

