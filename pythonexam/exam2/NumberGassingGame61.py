import random


def random_game():
    random_num = random.randint(1, 100)  # Generate a random number between 1 and 1000
    tries = 0

    while True:
        user_input = int(input("Guess the number (between 1 and 100): "))
        tries += 1

        if user_input == random_num:
            print(f"Congratulations! Correct number {random_num}.")
            print(f"Tries {tries} ")
            break
        elif user_input < random_num:
            print("Too low.")
        else:
            print("Too high.")


random_game()
