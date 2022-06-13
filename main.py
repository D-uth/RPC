import random

while True:
    user = input(" pick a guess: 'R' for rock, 'P' for paper, 'S' for Scissors")
    actions = ["R", "P", "S"]
    if user in actions:
        computer_action = random.choice(actions)
        print("Player (" + user + ") : CPU (" + computer_action + ")")
    else:
        print("enter a valid option. 'R' for rock, 'P' for paper, 'S' for Scissors")    
        

    if user == computer_action:
        print(f"Both players selected {user}. It's a tie!")
    elif user == "R":
        if computer_action == "S":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user == "P":
        if computer_action == "R":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user == "S":
        if computer_action == "P":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

    