import random

class Person:
    
    # Static counter for group
    
    def __init__(self, group_type, chanceToFindInfected=10, infectionRate=10):
        self.group_type = group_type
        self.boat_found = False
        self.is_fighting = False
        self.has_weapon = False
        self.has_vaccine = False
        self.infected = False
        self.chanceToFindInfected = chanceToFindInfected
        self.infectionRate = infectionRate
        self.seed_value = random.seed()
        if group_type == "recovered":
            self.infectionRate = 0
        else:
            self.infectionRate = infectionRate



    def Fight(self):
        originalInfectionRate = infectionRate
        if self.has_weapon:
            if (infectionRate - 20) >= 0:
                infectionRate -= 20
            else:
                infectionRate -= infectionRate
                
        return not (random.randint(1, 100) <= infectionRate)
            
            # Susceptible.count -= 1              # susceptible killed
            # Infected.count += 1
        # else:
        #     Infected.count -= 1                 # infected killed
        #infectionRate = originalInfectionRate

    def GatherResults(self, seed_value):
        outcome = self.Forage(seed_value)
       
        if outcome == 1:
            self.boat_found = True
        elif outcome == 2:
            self.has_weapon = True
        elif outcome == 3:
            self.has_vaccine = True
         
        print(f"Chance to find infected: {Susceptible.chanceToFindInfected}") # ! chanceToFindInfected not increasing correctly
        if self.InfectedFound():
            self.is_fighting = True
        if self.boat_found == True and self.is_fighting == False:
            self.Escape()
  

    def Forage(self, seed_value):
        outcome = random.seed(seed_value)
        outcome = random.randint(1,4)    
        return outcome
    
    def InfectedFound(self):
        return random.randint(0, 100) <= self.chanceToFindInfected
    
class Susceptible(Person): 
    group_count = 0   
    def GiveVaccine():
        if Infected.group_count > 0:
            return True


class Recovered(Person):
    group_count = 0

class Infected():
    group_count = 0

class Escapee():
    group_count = 0

class Dead():
    group_count = 0



def Escape(self):
    Susceptible.group_count -= 1
    Escapee.group_count += 1





def simulate():
    TOTAL_POPULATION = 50
    initial_susceptible = 45

    susceptible_lst = []
    infected_lst = []
    recovered_lst = []
    escapee_lst = []
    dead_lst = []

    # populate starting objects
    for i in range(initial_susceptible):
        susceptible_lst.append(Susceptible("susceptible"))
        Susceptible.group_count += 1
    for i in range(TOTAL_POPULATION - initial_susceptible):
        Infected.group_count += 1
        infected_lst.append(Infected())
        

    # print(Susceptible.group_count)
    # print(Infected.group_count)


simulate()
