import random
import math

red = "\u001b[31m"
green = "\u001b[32m"
cyan = "\u001b[36m"
yellow = "\u001b[33m"
orange = "\u001b[38m"
reset_color = "\u001b[0m"

name = input("\nHi, what is your name? ")
print(f"\nHi, {name}. Let's begin!")

def get_valid_input(prompt, min_value, max_value):
    while True:
        user_input = input(prompt)
        try:
            number = int(user_input)
            if min_value <= number <= max_value:
                return number
            else:
                print(f"\nInput must be between {min_value} and {max_value}.")
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")

def play_game():
        min_value = 100
        max_value = 1000
        number_one = get_valid_input(f"\nEnter a number ≥ {min_value}: ", min_value, max_value)
        number_two = get_valid_input(f"\nEnter a number ≤ {max_value}: ", min_value, max_value)

        minimum_number_of_guessing = 1 + math.log2(number_two - number_one + 1)
        max_attempts = math.ceil(minimum_number_of_guessing)
        
        print(f"\n{cyan}I have selected a magic number between {red}{str(number_one)}{cyan} and {red}{str(number_two)}{cyan}.{reset_color}")

        magic_number = random.randint(number_one, number_two)
        new_attempts = max_attempts
        while new_attempts > 0 :
            print(f"\nYou have {red}{str(new_attempts)}{reset_color} attempts left.")
            guess_str = input("\nGuess: ")
        
            try:
                guess_check = float(guess_str)
            except ValueError:
                print (f"\n{red}Please enter a valid number.{reset_color}")
                continue    

            if guess_check < magic_number:
                print(f"\n{yellow}Oops. Looks like your guess was {red}less{yellow} than the magic number. Try again. {reset_color}")
            elif guess_check > magic_number:
                print(f"\n{yellow}Oops. Looks like your guess was {red}more{yellow} than the magic number. Try again. {reset_color}")
            else:
                print(f"\n{green}Hooray! You guess the magic number: {str(magic_number)}{reset_color}\n")
                break

            new_attempts -= 1
        
        if new_attempts == 0:
            print(f"\nYou have run out of attempts. The magic number was {str(magic_number)}.\n")

if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break