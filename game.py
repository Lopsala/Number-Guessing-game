import random
print("Number Guessing Game")
number=random.randint(1,9)
chances=0
print("Guess the number in between 1 and 9")
while chances<5:
    guess=int(input("Enter your guess:"))
    if guess==number:
        print("Congratulations, you won!")
        break
    elif guess<number:
        print("Your guess was too low:Guess a number higher than ",guess,":")
    else:
        print("Your guess was too high:Guess a number lower than ",guess,":")
    chances+=1
if not chances<5:
    print("You lose! The number is ",number)