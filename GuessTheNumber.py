# This is a Guess the Number

import random

print("Hello! What's your name?")
myName = input()
number = random.randint(1, 20)
guessesTaken = 0
print("My name is " + myName)
print(f"Well, {myName}, I am thinking of a number between 1 to 20")

for guessesTaken in range(6):
    print("Take a guess.")      #Four spaces in front of print()
    guess = int(input())
    
    if guess < number:
        print("Your guess is too low.")     #8 spaces in front of print
        
    if guess > number:
        print("Your guess is too high.")
        
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print(f"Good job, {myName}!. You guessed my number in {guessesTaken} guess!.")
else:
    print(f"Nope. The number I was thinking of was {str(number)}.")
