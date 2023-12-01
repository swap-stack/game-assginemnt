
from enum import Enum
import time
import random


class GunChoices(Enum):
    """ Choices of Guns available"""
    SHORTGUN = 1
    PISTOL = 2


class Game:
    """ Manages the game logic """

    def __init__(self) -> None:
        self.total_points = 0
        self.selected_gun = None
        self.targets = []

    def spawn(self):
        print("You can see an alien in the distance.......")
        
        animals_display = ["🐇", "🦆"]
        
        for emoji in animals_display:
            self.targets.append(Animal(display=emoji))

        for _ in range(1):
            alien = Alien()
            self.targets.append(alien)

    def display_targets(self):
        print(self.targets)

    def select_gun(self, choice):
        """ Selects the type of gun a user wants to play with"""
        if choice == 1:
            self.selected_gun = Gun(name= GunChoices.SHORTGUN)
        elif choice == 2:
            self.selected_gun = Gun(name=GunChoices.PISTOL)

    def shoot(self, target_index):
        """ Simmulates shooting of an alien"""

        if 0 <= target_index < len(self.targets):
            if isinstance(self.targets[target_index], Alien):
                # print(f"Bullseye! +{self.selected_gun.damage} points")
                # self.total_points += self.selected_gun.damage
                self.total_points += 10

            else:
                print("Missed! -5 points")
                self.total_points -= 5
            self.targets.pop(target_index)

        else:
            print('Invalid Target')
        

        # if self.selected_gun:
        #     damage = self.selected_gun.damage
        #     alien.health -= damage
        #     if alien.health <= 0:
        #         print("Alien dead")
        #         del alien

    def play(self):
        print('')
        self.spawn()
        while self.targets:
            self.display_targets()
            try:
                target_index = int(input("Enter the index to shoot (0-3): "))
                self.shoot(target_index=target_index)
            except ValueError:
                print("Invalid input. Enter a number")
            time.sleep(1)
        print(f'Game over Your score is: {self.total_points} points')


    def stop(self):
        print('Game stopped')


class Animal:
    """ Represents the Animal in the game"""

    def __init__(self, display) -> None:
        self.display = display
        # self.damage = 5
        # self.health = 10

    def __repr__(self) -> str:
        return f"{self.display}"


class Alien:
    """ Represents the Alien in the game"""

    def __init__(self) -> None:
        self.display = "😈"
        # self.damage = 5
        # self.health = 10

    def get_damage(self):
        return self.damage


    def __repr__(self) -> str:
        return f"{self.display}"


class Gun:
    """ Represents a Weapon called Gun and its associated logic"""
    def __init__(self, name=GunChoices.PISTOL) -> None:
        self.name = name
        if self.name == GunChoices.PISTOL:
            self.damage = 3
        elif self.name == GunChoices.SHORTGUN:
            self.damage = 5


    def get_damage(self):
        """ Returns the damage of the Gun"""
        return self.damage

    def get_name(self):
        """Returns the name of the gun"""
        return self.name


class Player:
    """User playing the game"""
    def __init__(self, name) -> None:
        self.name = name
        self.health = 15



if __name__ == '__main__':
    choice= input("Do you want to play? Y/N")
    if choice == 'Y':
            # user_name = input("What is your character name")
            # user = Player(name= user_name)
        game = Game()
        game.play()
    else:
        print('Ok Bye')







