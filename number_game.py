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

min_value = 1000

max_value = 100

while True:

    upper_input = input(f"\nEnter a number > {str(min_value)}: ")

    try:
        number_1 = int(upper_input)
        if number_1 > min_value:
            break

        else:
            print(f"{yellow}\nInput must be greater than {str(min_value)}{reset_color}")
    
    except ValueError:
        print(f"{red}\nInvalid input. Please enter a valid number.{reset_color}")

print(f"{green}\nValid input: {str(number_1)}{reset_color}")

while True:
    lower_input = input(f"\nEnter a number < {str(max_value)}: ")

    try:
        number_2 = int(lower_input)
        if number_2 < max_value:
            break

        else:
            print(f"{yellow}\nInput must be less than {str(max_value)}{reset_color}")

    except ValueError:
        print(f"{red}\nInvalid input. Please enter a valid number.{reset_color}")
    
print(f"\n{green}Valid input: {str(number_2)}{reset_color}")

upperbound = int(number_1)

lowerbound = int(number_2)

minimum_number_of_guessing = 1 + math.log2(upperbound - lowerbound + 1)

rounded_up = math.ceil(minimum_number_of_guessing)

rounded_up_number = str (rounded_up)

selection = print(f"\n{cyan}I have selected a magic number between {red}{str(number_2)}{cyan} and {red}{str(number_1)}{cyan}.{reset_color}")

magic_number = random.randint(number_2, number_1)

max_attempts = int(rounded_up_number)

attempts = max_attempts

while attempts > 0 :
    
    print(f"\nYou have {red}{str(attempts)}{reset_color} attempts left.")

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
    
    attempts -= 1

if attempts == 0:

    print(f"\n{red}You have ran out of attempts. Try again next time!{reset_color}\n")



