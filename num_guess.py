# Author: Clara Hunt
# Github username: huntcl
# Date: 04/15/26
# Description: Number guessing game

target = int(input("Enter the integer for the player to guess:\n"))

guess = int(input("Enter your guess:\n"))

count = 1

while guess != target:
    if guess > target:
        guess = int(input("Too high - try again:\n"))
    else:
        guess = int(input("Too low - try again:\n"))

    count = count + 1

# after loop ends (correct guess)
if count == 1:
    print("You guessed it in 1 try.")
else:
    print("You guessed it in", count, "tries.")
