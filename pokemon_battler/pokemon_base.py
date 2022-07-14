"""
Author: Philip Ooi
Last Modified: 18 September 2021
This program is the Abstract parent class of the pokemon class (pokemon.py)
"""
from abc import ABC, abstractmethod

class PokemonBase(ABC):
    # An example of a base value for a stat
    BASE_LEVEL = 1 #set base level class variable (known and const to all children)
    def __init__(self, hp: int, poke_class: str):
        #hp checks and if hp is allowed
        if hp >= 0:
            self.hp = hp
        else:
            raise ValueError("HP cannot be below 0")

        #poke_class, put capitals for class_effectiveness later 
        if poke_class == "GRASS" or poke_class == "FIRE" or poke_class == "WATER":
            self.poke_class = poke_class
        else:
            raise TypeError("There is no such class")
        pass

    def get_hp(self):
        return self.hp



    @abstractmethod 
    def get_level(self):
        pass

    def get_poke_class(self):
        return self.poke_class


    def is_fainted(self):
        if self.hp <= 0:
            return True
        return False


    @abstractmethod
    def level_up(self):
        pass

    @abstractmethod
    def get_speed(self):
        pass

    @abstractmethod
    def get_attack_damage(self):
        pass

    @abstractmethod
    def get_defence(self):
        pass

    @abstractmethod
    def defend(self, damage: int):
        pass

    @abstractmethod
    def get_poke_name(self):
        pass

    def lose_hp(self,lost_hp:int) -> None:
        self.hp -= lost_hp
        pass

    def __str__(self): 
        pass

