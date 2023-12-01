
import time
import random
from characters import Alien, Animal
from weapons import Gun, GunChoices

class Game:
    """ Manages the game logic """

    def __init__(self) -> None:
        self.total_points = 0
        self.selected_gun = None
        self.targets = []

    def spawn(self):
        print("You can see an alien in the distance....... or is it??")
        
        animals_display = ["🐇", "🦆"]
        
        for emoji in animals_display:
            self.targets.append(Animal(display=emoji))

        for _ in range(1):
            alien = Alien()
            self.targets.append(alien)
        random.shuffle(self.targets)

    def display_targets(self):
        random.shuffle(self.targets)
        print(self.targets)

    def select_gun(self):
        """ Selects the type of gun a user wants to play with"""
        choice = int(input("Select a gun: \n1.Shortgun\n2.Pistol\nEnter your choice (1-2) ╾━╤デ╦︻ (▀̿ĺ̯▀̿ ̿): "))
        if choice == 1:
            self.selected_gun = Gun(name= GunChoices.SHORTGUN)
        elif choice == 2:
            self.selected_gun = Gun(name=GunChoices.PISTOL)

    def shoot(self, target_index):
        """ Simmulates shooting of an alien"""
        print(f"\n\n\n{self.selected_gun}\n\n\n")
        if 0 <= target_index < len(self.targets):
            if isinstance(self.targets[target_index], Alien):
                self.targets[target_index].health -= self.selected_gun.damage
                self.total_points += self.selected_gun.damage
                print(f"Bullseye! +{self.selected_gun.damage} points, Alien Health {self.targets[target_index].health}")

                if self.targets[target_index].health <=0:
                    self.targets.pop(target_index)

            else:
                print("Missed! -5 points")
                self.total_points -= 5
                self.targets.pop(target_index)

            random.shuffle(self.targets)

        else:
            print('Invalid Target')
 
 
    def play(self):
        print('')
        self.spawn()
        self.select_gun()
        while any(type(obj) == Alien for obj in self.targets):
            self.display_targets()
            if len(self.targets) == 1:
                time.sleep(1)
                print("Oh Uh.. Game Over!!")
                break
            try:
                target_index = int(input("Enter the index to shoot (0-3): "))
                self.shoot(target_index=target_index)
            except ValueError:
                print("Invalid input. Enter a number")
            time.sleep(1)
        print(f'Game over Your score is: {self.total_points} points')


    def stop(self):
        print('Game stopped')



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







