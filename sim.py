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
        # self.seed_value = random.seed()
        random.seed() # change seed value based of system time
        if group_type == "recovered":
            self.infectionRate = 0
        else:
            self.infectionRate = infectionRate


    # Used by susceptible and recovered classes but recovered always returns True (win fight)
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
        # infectionRate = originalInfectionRate
        
    # Susceptible and recovered both gather and can escape the island.
    # Recovered has no need for weapons bc they win fight 100% of the time
    # Vaccine can be used by both Susceptible and recovered
    def Gather(self):
        outcome = self.Forage()
       
        if outcome == 1:
            self.boat_found = True
        elif outcome == 2:
            self.has_weapon = True
        elif outcome == 3:
            self.has_vaccine = True
         
        # print(f"Chance to find infected: {self.chanceToFindInfected}") # ! chanceToFindInfected not increasing correctly
        if self.InfectedFound():
            self.is_fighting = True # is fighting if infected found (recovered skip fighting state and instantly kill infected or 10% loss)
        if self.boat_found == True and self.is_fighting == False: # can only escape if not fighting 
            if self.group_type == "susceptible":
                Escape(Susceptible)
            else:
                Escape(Recovered)
  
    # Dice roll to determine gather results only 1 item can be found at a time
    def Forage(self):
        return random.randint(1,4)    
        
    
    # if roll is less than or equal to threshold infectedFound = True
    def InfectedFound(self):
        return random.randint(0, 100) <= self.chanceToFindInfected
    
class Susceptible(Person): 
    group_count = 0   
    def GiveVaccine(self):
        if Infected.group_count > 0 and self.has_vaccine == True:
            # return True
            Infected.group_count -= 1
            Recovered.group_count += 1


class Recovered(Person):
    group_count = 0

class Infected():
    group_count = 0

class Escapee():
    group_count = 0

class Dead():
    group_count = 0



def Escape(group):
    group.group_count -= 1
    Escapee.group_count += 1





def simulate():
    # temp hard code values. 
    TOTAL_POPULATION = 50
    initial_susceptible = 45
    step = 0
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
        
    # Start simulation steps 
    # while len(susceptible_lst) > 0 or len(recovered_lst) > 0:
    while len(susceptible_lst) > 0:
        step += 1
        for sus in susceptible_lst:
            sus.Gather()
            sus.GiveVaccine()
        for rec in recovered_lst:
            rec.Gather()    
        print("step " + str(step))
        print("Susceptible count: " + str(Susceptible.group_count))
        print("Recovered count: " + str(Recovered.group_count))
        print("Infected count: " + str(Infected.group_count))
        print("Dead count: " + str(Dead.group_count))
    
    
    # logging
    

simulate()
