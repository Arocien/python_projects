"""
__author__ = "Philip Ooi"
__last_modified__ = "18.09.2021"
This program sets the children class of pokemon_base. Specifying the different types of pokemon
and their different specifications
"""

from pokemon_base import PokemonBase

class Charmander(PokemonBase):
    """
    Sets the base stats and methods of the charmander class 
    """
    #dict of effectiveness, used for effectiveness[filter] multiplier 
    CLASS_EFFECTIVENESS = {
            "WATER": 0.5,
            "GRASS": 2,
            "FIRE": 1
        }


    def __init__(self):
        # TODO: Define the constructor
        PokemonBase.__init__(self,7,"FIRE") #set hp and class from parent
        #Child attributes = Level/Speed/Defence/Attack, set base stats 
        self.level = PokemonBase.BASE_LEVEL #set base level, will increase with method level_up
        self.speed = 8 
        self.defence = 4
        self.attack = 6 
        self.name = "Charmander"
            
    #child methods

    def get_level(self):
        return self.level


    def level_up(self):
        self.level = self.level + 1


    def get_speed(self):
        return self.speed + self.get_level()


    def get_attack_damage(self):
        return self.attack + self.get_level()


    def get_defence(self):
        return self.defence


    def defend(self, damage: int):
        if damage > self.defence:
            self.hp = self.hp - damage
        else:
            self.hp = self.hp - damage // 2


    def get_poke_name(self):
        return self.name #returns default name unless re-assigned 


    def __str__(self):
        return self.name + "'s health = " + str(self.get_hp()) + " and level = " + str(self.get_level())



class Bulbasaur(PokemonBase):
    """
    Sets base stats and methods of the Bulbasaur class
    """
    CLASS_EFFECTIVENESS = {
            "WATER": 2,
            "GRASS": 1,
            "FIRE": 0.5
        }
    def __init__(self):
        # TODO: Define the constructor
        PokemonBase.__init__(self,9,"GRASS") #set hp and class from parent
        #Child attributes = Level/Speed/Defence/Attack/ Name 
        self.level = PokemonBase.BASE_LEVEL #set base level, will increase with method level_up
        self.speed = 7 
        self.defence = 5
        self.attack = 5
        self.name = "Bulbasaur"
            
    #child methods

    def get_level(self):
        return self.level

    def level_up(self):
        self.level = self.level + 1 


    def get_speed(self):
        return self.speed + (self.level // 2)
 

    def get_attack_damage(self):
        return self.attack
  

    def get_defence(self):
        return self.defence
    

    def defend(self, damage: int):
        if damage > (self.defence + 5):
            self.hp = self.hp -  damage
        else:
            self.hp -= damage // 2

    def get_poke_name(self):
        return self.name #returns default name unless re-assigned 
    
    
    def __str__(self):
        return self.name + "'s health = " + str(self.get_hp()) + " and level = " + str(self.get_level())

class Squirtle(PokemonBase):
    """
    Sets the base stats and methods of the Squirtle class
    """
    CLASS_EFFECTIVENESS = {
            "WATER": 1,
            "GRASS": 0.5,
            "FIRE": 2
        }

    def __init__(self):
        # TODO: Define the constructor
        PokemonBase.__init__(self,8,"WATER") #set hp and class from parent
        #Child attributes = Level/Speed/Defence/Attack
        self.level = PokemonBase.BASE_LEVEL #set base level, will increase with method level_up
        self.attack = 4 
        self.defence = 6
        self.speed = 7
        self.name = "Squirtle"

    #child methods

    def get_level(self):
        return self.level
   

    def level_up(self):
        self.level += 1 


    def get_speed(self):
        return self.speed + self.level // 2


    def get_attack_damage(self):
        return self.attack 
  

    def get_defence(self):
        return self.defence + self.level
     

    def defend(self, damage: int):
        if damage > self.defence * 2:
            self.hp = self.hp - damage
        else:
            self.hp = self.hp - damage // 2

    def get_poke_name(self):
        return self.name #returns default name unless re-assigned 
   

    def __str__(self):
        return self.name + "'s health = " + str(self.get_hp()) + " and level = " + str(self.get_level())
    

