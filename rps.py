# Rock Paper Scissors

import random

rps_options = {1: "ROCK", 2: "PAPER", 3: "SCISSORS"}

def print_game_result_message(cpu_choice, result):
    if result == "WIN":
        print("You won!, The CPU chose: " + cpu_choice)
    elif result == "DRAW": 
        print("The computer chose the same, it's a draw!")
    elif result == "LOSS":
        print("You lost... The CPU chose: " + cpu_choice)

while True:
    print("Choose ROCK, PAPER, SCISSORS // EXIT to leave the game.")
    user_choice = input()

    # Leave game if player chooses to do so
    if user_choice == "EXIT":
        break

    # Check is command is valid by checking every option to see if player has picked one 
    command_is_valid = False

    for key in rps_options:
        value = rps_options[key]
        if value == user_choice:
            command_is_valid = True
            break

    if not command_is_valid:
        print(f"Command '{user_choice} is not a valid command'")
        continue

    # Get computer choice
    random_int = random.randint(1, 3)
    computer_choice = rps_options[random_int]

    # Validate who won the game
    if (computer_choice == "ROCK" and user_choice == "ROCK"):
        print_game_result_message("ROCK", "DRAW")


