import random
import time

def generate_number():
    return random.randint(1, 100)

number = generate_number()
guesses = 0
games = 0
total_guesses = 0
attempts = 0

while True:
    guess = input("Guess a number: ")
    if guess == 'quit':
        print("Thanks for playing!")
        exit()
    try:
        guess = int(guess)
    except ValueError:
        print("Sorry, please put in a number!")
        attempts += 1
        time.sleep(1)
        if attempts >= 5:
            print()
            print()
            print("Sorry, please try again later.")
            exit()
        continue
    attempts = 0
    total_guesses += 1
    guesses += 1
    if guess == number:
        print(f"You guessed right! It took {guesses} guesses!")
        continue_game = input("Do you want to continue? yes or no: ").lower()
        games += 1
        while continue_game not in ('yes', 'no'):
            print("Sorry 'yes' or 'no' only!")
            continue_game = input("Do you want to continue? yes or no:  ").lower()
        if continue_game == 'yes':
            guesses = 0
            number = generate_number()
            continue 
        elif continue_game == 'no':
            stats = input("Would you like to see your stats? yes or no:  ").lower()
            while stats not in ('yes', 'no'):
                print("Sorry 'yes' or 'no' only!")
                stats = input("Do you want to continue? yes or no:  ").lower()
            if stats == 'yes':
                if games == 1:
                    print(f"You played {games} time! Guessed {total_guesses} times!")
                else:
                    print(f"You played {games} times! Guessed {total_guesses} times!")
                exit()
            elif stats == 'no':
                print("Thank you for playing!")
                exit()
            
    elif guess >= number:
        print("Too high!")
        continue
    elif guess <= number:
        print("Too low!")
        continue
    
