# -----------------------------------
# 2/6/2019
# From: Impractical Python Projects
# Chapter 1 - Silly Name Generator
# Obj: Randomly generate funny sidekick names using Python code
#      that conforms to established style guidelines
#
#  Psuedocode:
#     Load a list of first names
#     Load a list of surnames
#     Choose a first name at random
#     Assign the name to a variable
#     Choose a surname at random
#     Assign the name to a variable
#     Print the names to the screen in order and in red font
#     Ask the user to quit or play again
#     If user plays again:
#          repeat
#     If user quits:
#          end and exit
# -----------------------------------
"""Generate funny names by randomly combining names from 2 separate lists."""
import random


def main():
    """Choose names at random from 2 tuples of names and print to screen."""
    print("Welcome to Potter's Name Generator. Here's your Harry Potter inspired name:")

    first_names = ('Harry', 'Lily', 'James', 'Remus', 'Teddy', 'Ron',
                   'Hermione', 'Severus', 'Albus', 'Aberforth', 'Vernon',
                   'Dudley', 'Neville', 'Frank', 'Alice', 'Minerva',
                   'Kingsley', 'Bellatrix', 'Narcissa', 'Draco')

    last_names = ('Potter', 'Snape', 'Granger', 'Weasley', 'Lupin',
                  'Lestrange', 'Dumbledore', 'Longbottom', 'McGonagall',
                  'Dursley', 'Shacklebolt', 'Moody', 'Malfoy', 'Crabbe',
                  'Goyle')

    while True:
        first = random.choice(first_names)
        last = random.choice(last_names)
        print("\n")
        print(f"{first} {last}")
        print("\n")
        resp = input("Would you like to play again? Enter Y to play again, any other key to quit. >> ")
        if resp not in "Yy":
            break
    print("Thank you for playing!")


if __name__ == "__main__":
    main()
     