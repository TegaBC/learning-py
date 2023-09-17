import random

random_number = random.randint(1, 10)
max_guesses = 3
total_guesses = 0


print("Guess the random number (1 to 10)")

while True:
    user_answer = input()

    if int(user_answer) == random_number:
        print("You got the number correct.")
    else:
        total_guesses += 1
        print(f"Wrong, {total_guesses}/{max_guesses} guesses used.")

        if max_guesses == total_guesses:
            print(f"The number was {random_number}, better luck next time...")
            break