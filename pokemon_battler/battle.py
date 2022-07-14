"""
__author__ = "Philip Ooi"
__last_modified__ = "18.09.2021"
This program implements the Battle class which allows the pokemon in each stack/queue to battle 
"""

from poke_team import PokeTeam
from pokemon import Charmander, Bulbasaur, Squirtle

class Battle:
    """
    This class implements the methods set_mode_battle and __conduct_combat which allows the pokemon 
    from each stack/queue to fight based on their battle mode 

    """
    # TODO: Implement the battle class
    def set_mode_battle(self, player_one: str, player_two: str) -> int:
        """This method creates two instances of PokeTeam() and implements the method of choose_team and __conduct_combat 
        :pre: Two strings of the players
        :post: Battle between chosen amount of pokemon from both sides, returns 0(draw), 1(player 1 win) or 2(player 2 win)
        :complexity: O(choose_team)O(choose_team)O(__conduct_combat)
        """
        p1 = PokeTeam()
        p2 = PokeTeam()
        p1.choose_team(player_one,0)
        p2.choose_team(player_two,0)
        #battle_type = input("Set battle type: 1/0: ")
        return self.__conduct_combat(p1,p2,0)

    
    #queue battle
    def rotating_mode_battle(self, player_one: str, player_two: str) -> int:
        """This method creates two instances of PokeTeam() and implements the method of choose_team and __conduct_combat 
        :pre: Two strings of the players
        :post: Battle between chosen amount of pokemon from both sides, returns 0(draw), 1(player 1 win) or 2(player 2 win)
        :complexity: O(choose_team)O(choose_team)O(__conduct_combat)
        """
        p1 = PokeTeam()
        p2 = PokeTeam()
        p1.choose_team(player_one,1)
        p2.choose_team(player_two,1)
        return self.__conduct_combat(p1,p2,1)

    def __conduct_combat(self, team1: PokeTeam, team2: PokeTeam, battle_mode: int) -> int:
        """
        This method conducts the combat between the two pokemon 
        :pre:There must be two non-empty ArrayR with Pokemon inside
        :post: Returns 0 (draw), 1(player 1 win), 2(player 2 win)
        :complexity: Best case is O(1) where both stacks are empty or single pokemon of same type in each 
                     Worst case is O(n) where n is the number of pokemon from the SMALLER stack 

        """
        assert battle_mode == 0 or battle_mode == 1, "Battle Mode can only be 1 or 0"
        if battle_mode == 0:
            #asssert poke1 > 0 
            #check that BOTH are not empty otherwise it will throw an empty stack error 
            while team1.team.is_empty() != True and team2.team.is_empty() != True:
                poke1 = team1.team.pop()
                poke2 = team2.team.pop()
                #speed check

                #poke2 attack, poke1 defend
                if(poke1.get_speed() < poke2.get_speed()):
                    poke_type_mult = poke1.get_poke_class()
                    damage = poke2.get_attack_damage() * poke2.CLASS_EFFECTIVENESS[poke_type_mult]
                    poke1.defend(damage)

                    #pushing and fainting
                    if(not poke1.is_fainted() and not poke2.is_fainted()):
                        poke1.lose_hp(1)
                        poke2.lose_hp(1)
                        
                        if(poke1.is_fainted() and poke2.is_fainted()):
                            continue
                        
                        elif(poke1.is_fainted() == True):
                            poke2.level_up()
                            team2.team.push(poke2)

                            
                        elif(poke2.is_fainted() == True):
                            poke1.level_up()
                            team1.team.push(poke1)

                        
                        else:
                            team1.team.push(poke1)
                            team2.team.push(poke2)

                        
                        
                    elif(poke1.is_fainted()):
                        poke2.level_up()
                        team2.team.push(poke2)
                    else:
                        poke1.level_up()
                        team1.team.push(poke1)


                elif(poke1.get_speed() > poke2.get_speed()):
                    poke_type_mult = poke2.get_poke_class()
                    damage = poke1.get_attack_damage() * poke1.CLASS_EFFECTIVENESS[poke_type_mult]
                    poke2.defend(damage)

                    #pushing and fainting
                    if(not poke1.is_fainted() and not poke2.is_fainted()):
                        poke1.lose_hp(1)
                        poke2.lose_hp(1)
                        
                        if(poke1.is_fainted() and poke2.is_fainted()):
                            continue
                        
                        elif(poke1.is_fainted() == True):
                            poke2.level_up()
                            team2.team.push(poke2)

                            
                        elif(poke2.is_fainted() == True):
                            poke1.level_up()
                            team1.team.push(poke1)

                        
                        else:
                            team1.team.push(poke1)
                            team2.team.push(poke2)
                        
                    elif(poke1.is_fainted()):
                        poke2.level_up()
                        team2.team.push(poke2)
                    else:
                        poke1.level_up()
                        team1.team.push(poke1)

                else:
                    poke_type_mult = poke1.get_poke_class()
                    damage = poke2.get_attack_damage() * poke2.CLASS_EFFECTIVENESS[poke_type_mult]
                    poke1.defend(damage)
                    
                    poke_type_mult = poke2.get_poke_class()
                    damage = poke1.get_attack_damage() * poke1.CLASS_EFFECTIVENESS[poke_type_mult]
                    poke2.defend(damage)

                    #pushing and fainting
                    if(not poke1.is_fainted() and not poke2.is_fainted()):
                        poke1.lose_hp(1)
                        poke2.lose_hp(1)
                        
                        if(poke1.is_fainted() and poke2.is_fainted()):
                            continue
                        
                        elif(poke1.is_fainted() == True):
                            poke2.level_up()
                            team2.team.push(poke2)

                            
                        elif(poke2.is_fainted() == True):
                            poke1.level_up()
                            team1.team.push(poke1)

                        
                        else:
                            team1.team.push(poke1)
                            team2.team.push(poke2)

                        
                    elif(poke1.is_fainted() and poke2.is_fainted()):
                        continue
                        
                    elif(poke1.is_fainted()):
                        poke2.level_up()
                        team2.team.push(poke2)
                    else:
                        poke1.level_up()
                        team1.team.push(poke1)


            
            #checking winner
            if(team1.team.is_empty() and team2.team.is_empty() == True):
                return 0
            elif(team1.team.is_empty() == True):

                return 2
            else:

                return 1
            
        if battle_mode == 1:
                    #asssert poke1 > 0 
                    #check that BOTH are not empty otherwise it will throw an empty stack error 
                    while team1.team.is_empty() != True and team2.team.is_empty() != True:
                        poke1 = team1.team.serve()
                        poke2 = team2.team.serve()
                        #speed check

                        #poke2 attack, poke1 defend
                        if(poke1.get_speed() < poke2.get_speed()):
                            poke_type_mult = poke1.get_poke_class()
                            damage = poke2.get_attack_damage() * poke2.CLASS_EFFECTIVENESS[poke_type_mult]
                            poke1.defend(damage)

                            #pushing and fainting
                            if(not poke1.is_fainted() and not poke2.is_fainted()):
                                poke1.lose_hp(1)
                                poke2.lose_hp(1)
                                
                                if(poke1.is_fainted() and poke2.is_fainted()):
                                    continue
                                
                                elif(poke1.is_fainted() == True):
                                    poke2.level_up()
                                    team2.team.append(poke2)

                                    
                                elif(poke2.is_fainted() == True):
                                    poke1.level_up()
                                    team1.team.append(poke1)

                                
                                else:
                                    team1.team.append(poke1)
                                    team2.team.append(poke2)

                                
                                
                            elif(poke1.is_fainted()):
                                poke2.level_up()
                                team2.team.append(poke2)
                            else:
                                poke1.level_up()
                                team1.team.append(poke1)


                        elif(poke1.get_speed() > poke2.get_speed()):
                            poke_type_mult = poke2.get_poke_class()
                            damage = poke1.get_attack_damage() * poke1.CLASS_EFFECTIVENESS[poke_type_mult]
                            poke2.defend(damage)

                            #pushing and fainting
                            if(not poke1.is_fainted() and not poke2.is_fainted()):
                                poke1.lose_hp(1)
                                poke2.lose_hp(1)
                                
                                if(poke1.is_fainted() and poke2.is_fainted()):
                                    continue
                                
                                elif(poke1.is_fainted() == True):
                                    poke2.level_up()
                                    team2.team.append(poke2)

                                    
                                elif(poke2.is_fainted() == True):
                                    poke1.level_up()
                                    team1.team.append(poke1)

                                
                                else:
                                    team1.team.append(poke1)
                                    team2.team.append(poke2)
                                
                            elif(poke1.is_fainted()):
                                poke2.level_up()
                                team2.team.append(poke2)
                            else:
                                poke1.level_up()
                                team1.team.append(poke1)

                        else:
                            poke_type_mult = poke1.get_poke_class()
                            damage = poke2.get_attack_damage() * poke2.CLASS_EFFECTIVENESS[poke_type_mult]
                            poke1.defend(damage)
                            
                            poke_type_mult = poke2.get_poke_class()
                            damage = poke1.get_attack_damage() * poke1.CLASS_EFFECTIVENESS[poke_type_mult]
                            poke2.defend(damage)

                            #pushing and fainting
                            if(not poke1.is_fainted() and not poke2.is_fainted()):
                                poke1.lose_hp(1)
                                poke2.lose_hp(1)
                                
                                if(poke1.is_fainted() and poke2.is_fainted()):
                                    continue
                                
                                elif(poke1.is_fainted() == True):
                                    poke2.level_up()
                                    team2.team.append(poke2)

                                    
                                elif(poke2.is_fainted() == True):
                                    poke1.level_up()
                                    team1.team.append(poke1)

                                
                                else:
                                    team1.team.append(poke1)
                                    team2.team.append(poke2)

                                
                            elif(poke1.is_fainted() and poke2.is_fainted()):
                                continue
                                
                            elif(poke1.is_fainted()):
                                poke2.level_up()
                                team2.team.append(poke2)
                            else:
                                poke1.level_up()
                                team1.team.append(poke1)


                    
                    #checking winner
                    if(team1.team.is_empty() and team2.team.is_empty() == True):
                        return 0
                    elif(team1.team.is_empty() == True):

                        return 2
                    else:

                        return 1            
       

if __name__ == "__main__":
    battle = Battle()
    print(battle.set_mode_battle("Ash","Grey"))
    


