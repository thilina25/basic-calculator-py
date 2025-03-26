import random

numbert_to_guess = random.randint(1, 100)

while True:
    try:
        guess = int(input("Enter a number between 1 and 100: "))
        if guess == numbert_to_guess:
            print('You guessed it right!')
            break
        elif guess < numbert_to_guess:
            print('Guess higher')
        else:
            print('Guess lower')
    except ValueError:
        print('Invalid input. Please enter a number between 1 and 100')
