
from enum import Enum


class GunChoices(Enum):
    """ Choices of Guns available"""
    SHORTGUN = 1
    PISTOL = 2

class Gun:
    """ Represents a Weapon called Gun and its associated logic"""
    def __init__(self, name=GunChoices.PISTOL) -> None:
        self.name = name
        if self.name == GunChoices.PISTOL:
            self.damage = 5
        elif self.name == GunChoices.SHORTGUN:
            self.damage = 10


    def get_damage(self):
        """ Returns the damage of the Gun"""
        return self.damage

    def get_name(self):
        """Returns the name of the gun"""
        return self.name

    def __repr__(self) -> str:
        return f"...  ╾━╤デ╦︻"