# Developed by Elgiz Ibrahimli
# Date: 25.06.2018
# TechAcademy

import inquirer
from itertools import count
from random import randint
from math import isclose

# This is user total score - which will hold the user scores
score = 0

# Greeting message
print("*" * 24)
print("Welcome! To Number Game!")
print("*" * 24)

# Generator for random numbers - getting random numbers between 1,50 - 5 times
mygen = (randint(1, 50) for _ in range(5))
# Creating list of random numbers from generator object
mygen_list = list(mygen)

# Creating infinite loop
for _ in count(start=1, step=1):
    # Looping through random number list
    for mynum in mygen_list:
        print("#" * 10)
        # Asking user to type number, input 5 times for each random number mynum.
        for _ in range(5):
            questions = [inquirer.Text('num', message="Please enter a number",
                                            validate=lambda _, x: isinstance(int(x), int) is True)]
            answers = inquirer.prompt(questions)
            your_answer = answers['num']

            if mynum == int(your_answer):
                # If user found the number increase the score by 1
                score += 1
                print("Found the number!")
                break
            else:
                if isclose(mynum, int(your_answer), rel_tol=0.2):
                    print("You are close to the number!")
                else:
                    print("You are away from the number!")
    
    print("This is your score: ", score)
    questions = [inquirer.Confirm('continue',
                    message="Do you want to start new game?")]
    answers = inquirer.prompt(questions)
    if answers['continue']:
        print("Starting new Game!")
        # Making score to be equal to zero - to make it clean.
        score = 0
        # Generating new 5 random numbers
        mygen = (randint(1, 50) for _ in range(5))
        # Creating new list from new random numbers
        mygen_list = list(mygen)
    else:
        print("Thanks for your game!")
        break

    