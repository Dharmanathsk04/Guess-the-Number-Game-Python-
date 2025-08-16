import random

print("🎲 Welcome to Guess the Number Game!")
print("I have picked a number between 1 and 20. Can you guess it?")

# computer picks a random number
secret = random.randint(1, 20)

while True:
    guess = int(input("Enter your guess: "))

    if guess == secret:
        print("🎉 Correct! You guessed the number!")
        break
    elif guess < secret:
        print("Too low, try again!")
    else:
        print("Too high, try again!")
