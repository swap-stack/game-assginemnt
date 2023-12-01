
import time
import random
from characters import Alien, Animal, Player

class Game:
    """ Manages the game logic """

    def __init__(self, player) -> None:
        self.player = player
        self.player.gun = None
        self.targets = []

    def spawn(self):
        """Spawn some aliens and animals"""
        animals_display = ["🐇", "🦆"]
        
        for emoji in animals_display:
            self.targets.append(Animal(face=emoji))

        for _ in range(1):
            alien = Alien()
            self.targets.append(alien)
        random.shuffle(self.targets)

    def display_targets(self):
        """Displays all the current targets"""
        print("xxxxx............................................xxxx")
        print("You can see an alien in the distance....... or is it??")
        print("xxxxx............................................xxxx")

        random.shuffle(self.targets)
        targets = "              ".join([ i.face for i in self.targets])
        print(f"\n\n{targets}\n\n")

    def shoot(self, target_index):
        """Simmulates shooting with a gun"""
        print(f"\n\n{self.player.gun}\n\n")

        if 0 <= target_index < len(self.targets):
            if isinstance(self.targets[target_index], Alien):
                self.targets[target_index].health -= self.player.gun.damage
                self.player.total_points += self.player.gun.damage
                print(f"Bullseye! +{self.player.gun.damage} points, Alien Health {self.targets[target_index].health}\n")

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
        """Starts the Game"""
        print('')
        self.spawn()
        self.player.select_gun()
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
        """Represents ending the game"""
        print('Game stopped')


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







