
class Animal:
    """ Represents the Animal in the game"""

    def __init__(self, display) -> None:
        self.display = display
        # self.damage = 5
        # self.health = 30

    def __repr__(self) -> str:
        return f"{self.display}"


class Alien:
    """ Represents the Alien in the game"""

    def __init__(self) -> None:
        self.display = "😈"
        # self.damage = 5
        self.health = 30

    def get_damage(self):
        return self.damage

    def __repr__(self) -> str:
        return f"{self.display}"
