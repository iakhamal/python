# this is a short guessing program when it makes even humen or computer to guess the secret number 
import random

#making the user guess 
def guess_user (x):
    random_number=random.randint(1,x)
    guess = 0
    while guess != random_number :
        guess = int(input(f' guess a number between 1 and {x}\n'))
        if guess < random_number:
            print('\n you guess it wrong it too LOW please try again !!')
        elif guess > random_number:
            print("\n you guess it wrong it too HIGH please try again !!")
    print("\n well done it is the correct number YOU WIN !!")

guess_user(10)
#making the computer guess 
def guess_computer (x):
    low = 1
    high = x
    feedback = " "
    while feedback != " correct":
        if low != high :
            guess = random.randint (low , high)
        else :
            guess = low 
        feedback = input (f"is {guess} too high (high) , too low (low) , or correct (correst) ")
        if feedback == "high":
            high = guess - 1
        elif feedback == "low":
            low = low + 1 
guess_computer(200)
