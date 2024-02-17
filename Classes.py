import random
from Interface import *
class Character:
    def __init__(self, name, lvl = 1, race = 'human', item = 'none', gold = 0, silver = 0, copper = 0, hp ):
        self.name = name
        self.level = lvl
        self.race = race
        self.item = item
        self.gold = gold
        self.silver = silver
        self.copper = copper
        self.hp = hp

    #need rolling functions
  

    def levelUp(self,constitution,):
        self.level += 1
        hp = 0
        std::cout << "Enter 1 to roll for hp, 2 to take the fixed amount"
        std::cin >> input_
        if int(input_) == 1:
            std::cout << "What is your hit dice: 1d6, 1d8, 1d10, 1d12" << std::endl
            std::cin >> dice 
            if dice == '1d6':
                hp = rolld6() + constitution

            elif dice =='1d8':
                hp = rolld8() + constitution
            
            elif dice == '1d10':
                hp = rolld10() + constitution
            
            elif dice == '1d12':
                hp = rolld12() + constitution
            
            elif dice == '1d20':
                hp = rolld20() + constitution
            
            else:
                std::cout << "Invalid input, pls try 1d6, 1d8, 1d10, or 1d12"
        elif int(input_) == 2:
            std::cout << "What is your hit dice: 1d6, 1d8, 1d10, or 1d12" << std::endl







    
    

    






