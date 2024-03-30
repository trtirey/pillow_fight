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

    return players


def main_loop(players):
    two_players = True
    combatants = players
    current_combatant = 0
    while(two_players):
        # The current combatant swings
        print(f"{combatants[current_combatant].name} swings!")

        if (random() < 0.9):        # A hit!
            print("And hits!")
            if(random() < .02):     # Critical hit! Uh oh!
                combatants[current_combatant - 1].is_conscious = False
                print(f"Uh oh, {combatants[current_combatant].name} accidently knocked out {combatants[current_combatant - 1].name}!")
            else:
                if (random() < 0.5):
                    combatants[current_combatant].reduce_stamina()
        combatants[current_combatant].reduce_stamina()      # The player that swung gets tired!
        current_combatant = (current_combatant + 1) % 2

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

