# --------------------
#
# Monte Carlo simulation of Monty Hall problem
#
# --------------------

import random

def user_prompt(prompt, default=None):
    """Allow use of default values in input."""
    prompt = "{} [{}]".format(prompt, default)
    response = input(prompt)
    if not response and default:
        return default
    else:
        return response
    
print("This program will use a Monte Carlo Simulation to consider the Monty Hall problem.")
print("You're given a choice between 3 doors, you make a selection and your host opens one of the doors you didn't pick.")
print("You want to win a prize. Should you keep your choice or switch to the other door?")
print("Let's run a simulation to find out ...")
    
# input number of times to run simulation    
num_runs = int(user_prompt("\nHow many times should we run the simulation? (Type a number or press <Enter> for the default)", 20000))

# assign counters for ways to win
first_choice_wins = 0
pick_change_wins = 0
doors = ['a', 'b', 'c']

# run Monte Carlo
for i in range(num_runs):
    winner = random.choice(doors)
    pick = random.choice(doors)
    
    if pick == winner:
        first_choice_wins += 1
    else:
        pick_change_wins += 1
        
print("\nWins with original pick = {}; probability is {:.2f}".format(first_choice_wins, first_choice_wins/num_runs))
print("Wins with changed pick = {}; probability is {:.2f}".format(pick_change_wins, pick_change_wins/num_runs))
print("\nBased on the simulation it looks like you should change your pick. You double your chance of winning if you switch doors.")