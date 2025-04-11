

class Infected:
    infection_value = 0
    isInfected = True
    count = 0
    
    def __init__(self):
       pass 
    
    def vaccine(self):
        if self.infection_value < 60:
            Infected.count -= 1
            # Recovered.count += 1
        
        
       