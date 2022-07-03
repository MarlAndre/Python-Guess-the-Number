from art import logo
import random

EASY_LEVEL = 10
HARD_LEVEL = 5

# Check player guess against real number to guess
def check_guess(guess, number_to_guess, turns):
  """Return number of turn remaining"""
  if guess > number_to_guess:
    print("Too high")
    return turns - 1
  elif guess < number_to_guess:
    print("Too low")
    return turns - 1
  else:
    print (f"You win! The answer was {number_to_guess}.")

# Set level difficulty
def set_level():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == 'easy':
    return EASY_LEVEL
  else:
    return HARD_LEVEL

def guess_number():
  # Random number
  print(logo)
  print("Welcome to Number Guessing Game")
  
  print("I'm thinking of a number between 1 and 100")
  number_to_guess = random.randint(1, 100)

  # print(f"Test the code. Number to guess is {number_to_guess}")
  turns = set_level()

  # Repeat guess functionnality if player is wrong
  guess = 0
  while guess != number_to_guess:
    print(f"You have {turns} attempts remaining to get the right number.")

    guess = int(input("Make a guess: "))
    print("================================")

    # Track number of turns and reduce it by 1 if the player is wrong
    turns = check_guess(guess, number_to_guess, turns)
    if turns == 0:
      print("Game over. No remaining guesses left")
    elif guess != number_to_guess:
      print("Try again.")

guess_number()