from math import ceil, floor
from random import random

class Character():
    def __init__ (self, name, stamina=10, strength=10):
        self.name = name
        self.stamina = stamina
        self.strength = strength
        self.is_conscious = True

    def swing(self):
        return self.strength
    
    def get_stamina(self):
        return self.stamina
    
    # Reduce the characters stamina; If the characters stamina drops below 5, halve the characters strength, rounding up to the nearest integer.\
    # If the characters stamina is reduced to zero or less, the character lies down and takes a nap.
    def reduce_stamina(self, increment=1):
        if increment < self.stamina:
            self.stamina -= increment
            if self.stamina < 5:
                self.strength = ceil(self.strength / 2)
        else:
            self.stamina = 0
            self.is_conscious = False


def start_game():
    players = []
    for i in range(2):
        print("Enter the players name:")
        name = input()
        print("Enter the players stamina (we suggest no more than 20):")
        stamina = int(input())
        print("Enter the players strength (we recommend 10 or less):")
        strength = int(input())
        players.append(Character(name, stamina, strength))
    print("\nPress enter to continue")
    input()

    return players


##
# General game logic: players take turns swinging at each other (perhaps later implementing an alternative shielding action).
# 9 of 10 swings hit. If a swing hits, there's a 20% chance of a 'critical hit' that knocks out the hit player. If the swing
# doesn't crit, there's a 50% chance the hit character has their stamina reduced. The character that swung always has their stmina reduced.
##

def main_loop(players):
    two_players = True
    combatants = players
    current_combatant = 0
    while(two_players):
        # The current combatant swings
        print(f"{combatants[current_combatant].name} swings!")

        if (random() <= 0.9):        # A hit!
            print("And hits!")
            if(random() < .02):     # Critical hit!
                combatants[current_combatant - 1].is_conscious = False
                print(f"Uh oh, {combatants[current_combatant].name} accidently knocked out {combatants[current_combatant - 1].name}!")
            else:
                if (random() < 0.5):
                    combatants[current_combatant-1].reduce_stamina(ceil(.1 * combatants[current_combatant].strength))
        combatants[current_combatant].reduce_stamina()      # The player that swung gets tired!
        current_combatant = (current_combatant + 1) % 2     # Switch the current combatant

        # Check for unconscious player(s)
        for player in combatants:
            if player.is_conscious == False:
                two_players = False
        
        print("Press enter to continue")
        input()
    
    print("The players are all tired out!")






if __name__ == "__main__":
    print("Welcome to the Pillow Fight!")
    play = True
    while(play):
        players = start_game()
        main_loop(players)
        print("Play again? (y/n)")
        while(True):
            response = input()
            if response.lower() in ["n", "no"]:
                play = False
                break
            elif response.lower() in ['y', 'yes']:
                break
            else:
                print("I'm sorry, that wasn't a valid answer, try again!")




### Reference
""" import time
import os

# Print some information
print("Welcome to the game!")

# Wait for 5 seconds
time.sleep(5)

# Clear the command line
os.system('cls' if os.name == 'nt' else 'clear')

# Print an input prompt
user_input = input("Enter your name: ")

# Print the user's input
print("Hello, " + user_input + "!")  """           