from susceptible import Susceptible



class Recovered(Susceptible):
    count = 0
        
    def __init__(self, type, boat_found, is_fighting, has_weapon, has_vaccine, infected):
        #Recovered.count += 1
        Recovered.seed_value += 20
        super().__init__(self, type, boat_found, is_fighting, has_weapon, has_vaccine, infected)
    
    def GiveVaccine(self):
        Recovered.count += 1
        Susceptible.setInfectedCount(-1)
        
        
    # def run():
        
        
        
     