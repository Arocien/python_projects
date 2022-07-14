"""
__author__ = "Philip Ooi"
__last_modified__ = "18.09.2021"
This program implements the Battle class which allows the pokemon in each stack/queue to battle 
"""
from pokemon import Charmander, Bulbasaur, Squirtle
from stack_adt import ArrayStack
from queue_adt import CircularQueue

class PokeTeam:
    """
    This class sets a team that is specified by choose_team method

    """
    TEAM_LIMIT = 6
    def __init__(self):
        self.name = None
        self.team = None
        self.battle_mode = None
        
    #methods

    def choose_team(self, name: str, battle_mode: int) -> None:
        """
        Method sets team and number of each Charmander, Bulbasaur and Squirtle that is needed to be inputted
        Best and worst case is O(1) for input 
        """
        self.battle_mode = battle_mode
        self.name = name 

        #assign c b s
        print("Trainer " + self.name + " Choose your team as C B S" )
        print("Where C is the number of Charmanders")
        print("      B is the number of Bulbasaurs")
        print("      S is the number of Squirtles")
        c,b,s = input("->").strip().split()
        c = int(c)
        b = int(b)
        s = int(s)
        #check correct team 
        while(self.__correct_team_given(c,b,s) != True):
            print("Make sure your team has 1-6 pokemon, please try again! \n")
            print("Trainer " + self.name + " Choose your team as C B S" )
            print("Where C is the number of Charmanders")
            print("      B is the number of Bulbasaurs")
            print("      S is the number of Squirtles")
            c,b,s = input("->").strip().split()
            c = int(c)
            b = int(b)
            s = int(s)

        #assign correct team 
        self.__assign_team(self.name,c,b,s)
        print("Team Assigned: " + self.name)

    
    
    def __correct_team_given(self, charmanders: int, bulbasaurs: int, squirtles: int) -> bool:
        #x < 6 
        """
        Checks whether the team is correctly within the numbers of 0-6 otherwise return a False
        Best and Worst is O(1)O(1) from both addition and boolean comparison 
        """
        if(charmanders + bulbasaurs + squirtles <= PokeTeam.TEAM_LIMIT and charmanders >= 0 and bulbasaurs >= 0 and squirtles >= 0):
            return True
        return False




    def __assign_team(self, name:str, charmanders: int, bulbasaurs: int, squirtles:int) -> None:
        """
        Method sets team based on either stack or queue based on the battle mode specified. 
        Best and Worst case is O(n) where n is the number of Charmander, Bulbasaur and Squirtle
        """
        
        #use assert because it is accepting input 
        assert self.battle_mode == 1 or self.battle_mode == 0, "Battle mode can only be 1 or 0"
        self.name = name
        if self.battle_mode == 0:
        #create stack 
            self.team = ArrayStack(charmanders + bulbasaurs + squirtles)

            #pushing pokemon, check for 0 pokemon
            if (squirtles > 0):
                for _ in range(squirtles):
                    self.team.push(Squirtle())
            if (bulbasaurs > 0):
                for _ in range(bulbasaurs):
                    self.team.push(Bulbasaur())
            if (charmanders > 0):
                for _ in range(charmanders):
                    self.team.push(Charmander())
                    
        else:
            self.team = CircularQueue(charmanders + bulbasaurs + squirtles)
            if (charmanders > 0):
                for _ in range(charmanders):
                    self.team.append(Charmander())
            if (bulbasaurs > 0):
                for _ in range(bulbasaurs):
                    self.team.append(Bulbasaur())
            if (squirtles > 0):
                for _ in range(squirtles):
                    self.team.append(Squirtle())


                    
            
            

        
    def __str__(self): #print out the team 
        return str(self.team)

#testing files 
if __name__ == "__main__":  
    p1 = PokeTeam()
    p1.choose_team("HSA MUHCTEK",1)
    print(p1.__str__())

