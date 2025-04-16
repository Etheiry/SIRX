from forage import Forage
from infected import Infected
from escape import Escape



import random

class Susceptible:
    status = ""
    type = ""
    # instance variables (bool)
    boat_found = False
    is_fighting = False
    has_weapon = False
    has_vaccine = False
    infected = False
    
    # instance variables
    chanceToFindInfected = 0
    infectionRate = 10
    
    # keeps track of total susceptible count
    count = 0
    seed_value = 10
    
    
    def __init__(self, type, boat_found, is_fighting, has_weapon, has_vaccine, infected, chanceToFindInfected=0, infectionRate=10):
        self.type = type # either susceptible or recovered
        self.boat_found = boat_found
        self.is_fighting = is_fighting
        self.has_weapon = has_weapon
        self.has_vaccine = has_vaccine
        self.infected = infected
        self.chanceToFindInfected = chanceToFindInfected
        self.infectionRate = infectionRate
        
          
        
    
    def run(self):
        random.seed(self.seed_value + 10)
        self.GatherResults(self.seed_value)
        # self.GiveVaccine()
        if self.is_fighting and Infected.count > 0:
            self.Attack(self.infectionRate)
            # if self.type == "recovered":
            #     self.Attack(-1)
            # elif self.type == "susceptible":
            #     self.Attack(self.infectionRate)
            #Attack()
        self.seed_value += (self.seed_value.bit_count())
        
        
            
            
            
    def GatherResults(self, seed_value):
        outcome = Forage.gather(seed_value)
       
        if outcome == 1:
            self.boat_found = True
        elif outcome == 2:
            self.has_weapon = True
        elif outcome == 3:
            self.has_vaccine = True
        
        print(f"Chance to find infected: {Susceptible.chanceToFindInfected}") # ! chanceToFindInfected not increasing correctly
        if self.InfectedFound():
            self.is_fighting = True
        if self.boat_found == True:
            self.Escape()  
        
    def Escape(self):
        Susceptible.count -= 1              # susceptible converted to escapee
        Escape.count += 1                 # escapee created
    
    def InfectedFound(self):
        return random.randint(0, 100) <= self.chanceToFindInfected
    
    
    def Attack(self, infectionRate):
        originalInfectionRate = infectionRate
        if self.has_weapon:
            if (infectionRate - 20) >= 0:
                infectionRate -= 20
            else:
                infectionRate -= infectionRate
        
                
        if random.randint(1, 100) <= infectionRate:
            Susceptible.count -= 1              # susceptible killed
            Infected.count += 1
        # else:
        #     Infected.count -= 1                 # infected killed
        infectionRate = originalInfectionRate
    # def GiveVaccine():
    #     Infected.count -= 1
    #     Recovered.count += 1
    def setInfectedCount(num):
        Infected.count += num 