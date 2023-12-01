
import time
import random
from characters import Alien, Animal
from weapons import Gun, GunChoices

class Game:
    """ Manages the game logic """

    def __init__(self, player) -> None:
        self.player = player
        self.player.total_points = 0
        self.selected_gun = None
        self.targets = []

    def spawn(self):
        
        animals_display = ["🐇", "🦆"]
        
        for emoji in animals_display:
            self.targets.append(Animal(display=emoji))

        for _ in range(1):
            alien = Alien()
            self.targets.append(alien)
        random.shuffle(self.targets)

    def display_targets(self):
        print("xxxxx............................................xxxx")
        print("You can see an alien in the distance....... or is it??")
        print("xxxxx............................................xxxx")

        random.shuffle(self.targets)
        x = "              ".join([ i.display for i in self.targets])
        print(f"\n\n{x}\n\n")

    def select_gun(self):
        """ Selects the type of gun a user wants to play with"""
        choice = int(input("Select a gun: \n1.Shortgun\n2.Pistol\nEnter your choice (1-2) ╾━╤デ╦︻ (▀̿ĺ̯▀̿ ̿): "))
        if choice == 1:
            self.selected_gun = Gun(name= GunChoices.SHORTGUN)
        elif choice == 2:
            self.selected_gun = Gun(name=GunChoices.PISTOL)
        print(f"\n\nYou have chosen {self.selected_gun.get_name().name} {self.selected_gun} \n\n")

    def shoot(self, target_index):
        """ Simmulates shooting of an alien"""
        print(f"\n\n{self.selected_gun}\n\n")

        if 0 <= target_index < len(self.targets):
            if isinstance(self.targets[target_index], Alien):
                self.targets[target_index].health -= self.selected_gun.damage
                self.player.total_points += self.selected_gun.damage
                print(f"Bullseye! +{self.selected_gun.damage} points, Alien Health {self.targets[target_index].health}\n")

                if self.targets[target_index].health <=0:
                    self.targets.pop(target_index)

            else:
                print(f"Missed! -5 points {self.player.total_points}\n")
                self.player.total_points += -5
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
                print("Oh Uh.. Game Over You Lost!!")
                break
            try:
                target_index = int(input("Enter the index to shoot (0-3): "))
                self.shoot(target_index=target_index)
            except ValueError:
                print("Invalid input. Enter a number")
            time.sleep(1)


    def stop(self):
        print('Game stopped')


class Player:
    """User playing the game"""
    def __init__(self, name) -> None:
        self.name = name
        self.health = 15

    def display_points(self):
        print(f"{self.name} collected {self.total_points} points")


if __name__ == '__main__':
    choice= input("Do you want to play? Y/N")
    if choice == 'Y':
        user_name = input("Enter your character name:\n")
        user = Player(name=user_name)
        game = Game(player=user)
        game.play()
        user.display_points()
    else:
        print('Ok Bye')







