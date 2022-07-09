from random import randint

PLAYER: str = input("What is your name?\n")
TARGET: int = randint(1, 20)
lives: int = 6
total_guesses: int = 0

while (lives > 0):

    guess = int(input("Guess a number from 1 to 20:\n"))
    total_guesses += 1

    if guess == TARGET:
        print (f"Good job {PLAYER}! you guessed the number in {total_guesses} guesses!")
        break
    
    lives -= 1

    if guess > TARGET:
        print ("You guessed too high!")

    if guess < TARGET:
        print ("You guessed too low!")

    if lives == 1:
        print ("You ran out of lives!")
