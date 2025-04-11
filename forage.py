import random
class Forage():
    
    def gather(seed_value):
        
        outcome = random.seed(seed_value)
        outcome = random.randint(1,4)
        
        return outcome
    