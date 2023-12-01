from weapons import Gun, GunChoices

class Animal:
    """ Represents the Animal in the game"""

    def __init__(self, face) -> None:
        self.face = face
        # self.damage = 5
        # self.health = 30

    def __repr__(self) -> str:
        return f"{self.face}"


class Alien:
    """ Represents the Alien in the game"""

    def __init__(self) -> None:
        self.face = "😈"
        # self.damage = 5
        self.health = 30

    def get_health(self):
        return self.health

    def __repr__(self) -> str:
        return f"{self.face}"


class Player:
    """Represnts the user playing the game"""
    def __init__(self, name) -> None:
        self.name = name
        self.health = 15
        self.gun = None
        self.total_points = 0

    def select_gun(self):
        """Selects the type of gun a user wants to play with"""
        choice = int(input("Select a gun: \n1.Shortgun\n2.Pistol\nEnter your choice (1-2) ╾━╤デ╦︻ (▀̿ĺ̯▀̿ ̿): "))
        if choice == 1:
            self.gun = Gun(name= GunChoices.SHORTGUN)
        elif choice == 2:
            self.gun = Gun(name=GunChoices.PISTOL)
        print(f"\n\nYou have chosen {self.gun.get_name().name} {self.gun} \n\n")


    def display_points(self):
        """Displays the total points collected by the player"""
        print(f"{self.name} collected {self.total_points} points")
