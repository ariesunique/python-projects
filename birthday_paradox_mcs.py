#
# ---------------------------------
# Birthday Paradox: How many people need to be in a room for there to be a 
#     50 / 50 chance that two of them share the same birth month and day?
# Use a Monte Carlo simulation to find the answer.
#
# This is a suggested practice project from Chap 11 of Impractical Python Projects.
# The code here is my own code.
#
# Strategy:
#     There are 365 days in a year (ignoring leap years), so there are 
#     365 possibilies for a person to have a given birthday.
#     Randomly assign a person a number between 1 and 365 and add to a list.
#
# Probability calculation:
#    numerator = num people sharing the same birthday
#    denominator = num people in the room
#
# ---------------------------------

import random
import math


num_trials = 100000
results = []
for _ in range(num_trials):
    people = []
    done = False
    while not done:
        bday = random.randint(1, 365)
        if bday in people:
            done = True
        else:
            people.append(bday)
            
    results.append(len(people))
    
print("After {} trials, the average number of people required in a room for there to be a 50/50 chance that two share the same birthday is {:.0f}".format(num_trials, sum(results)/len(results)))

