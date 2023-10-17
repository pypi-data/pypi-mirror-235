import random
from .exceptions import OutOfRange

def start_guessing_game(lower_range = 1, upper_range = 100):
    random_number = random.randint(lower_range,upper_range+1)
    attempts = 1
    
    welcome_message = f"Hey! I've thought up a secret number between {lower_range} and {upper_range}.\nLet's see how many attempts it takes you to guess the secret correctly!!\n"
    print(welcome_message)

    while True:
        try:
            guess = int(input("Enter your guess: "))

            if guess < lower_range or guess > upper_range:
                raise OutOfRange(lower_range, upper_range)
            
            if guess == random_number:
                print(f"Congratulations you've guessed the number correctly in {attempts} attempts" )
                break
            elif guess < random_number:
                print("Your guess is smaller than the secret.")
            else:
                print("Your guess is larger thant the secret.")
            
            attempts += 1

        except ValueError as e:
            print(e)
            continue
        except OutOfRange as e:
            print(e)
            continue
