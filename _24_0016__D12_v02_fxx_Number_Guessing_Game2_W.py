#Number Guessing Game Objectives:

import random

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

# print(logo)

def play_Number_Guessing_game():

    turns_remaining = 0

    difficulty_level = int(input(f"Please choose between easy or hard (1 = easy, 2 = hard): "))
    if difficulty_level == 1:
        # global turns_remaining_for_easy
        # global turns_remaining
        turns_remaining += 10
    elif difficulty_level == 2:
        # global turns_remaining_for_hard
        # global turns_remaining
        turns_remaining += 5

    player_guessed_number = ""

    if difficulty_level == 1:
        print(f"You chose easy")
    else:
        print(f"You chose hard")

    base_number = int(random.randint(1, 100))

    continue_playing = True
    while continue_playing:

        # def base_number_determined():


        # print(f"The secret number is {base_number}")


        while turns_remaining > 0:
        # def player_guesses_number():
            player_guessed_number = int(input(f"Please guess a number between 1-100: "))

    # while continue_playing == True:

        # def redirect_higher_or_lower():
            if base_number > player_guessed_number:
                print(f"Guess higher")
            elif base_number < player_guessed_number:
                print(f"Guess lower")
            elif base_number == player_guessed_number:
                print("You guessed it perfectly right!! Wow!")
                continue_playing = False
                break
            turns_remaining -= 1
            print(f"The number of turns remaining is: {turns_remaining}")
        else:
            print(f"Womp womp. You ran out of turns. Game Over. The number was {base_number}.")
            continue_playing = False
            break


    # base_number_determined()

    # player_guesses_number()

    # redirect_higher_or_lower()


#play again?
while True:
    play_Number_Guessing_game()
    play_again_option = input("Do you want to play again? (Y or N): ").upper()
    if play_again_option != "Y":
        print("Okay, thank you for playing! Have a great day then!")
        break
