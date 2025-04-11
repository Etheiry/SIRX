from susceptible import Susceptible
from infected import Infected
from recovered import Recovered
from escape import Escape

import random


def main():
    initialPopulation = 50 
    Susceptible.count = 45 
    seedValue = input("Starting seed: ")
    #initialPopulation = input("Enter total population: ")
    #Susceptible.count = input("Enter initial Susceptible: ")
    Infected.count = initialPopulation - Susceptible.count   
    Recovered.count = initialPopulation - (Susceptible.count + Infected.count) 
    
    # testing numbers 
    
    stepCount = 1
    while stepCount <= 100:
        Susceptible.seed_value = stepCount * 3
        if(Susceptible.count > 0):
            susceptible = Susceptible("sus", False, False, False, False, False).run()
        #infected = Infected().run()
        recovered = Recovered("sus", False, False, False, False, False).run() 
         
        print(f"step: {stepCount}")
        print(f"Susceptible: {Susceptible.count}\ninfected: {Infected.count}\nrecovered: {Recovered.count}\nEscaped: {Escape.count}")
        print(f"total population: {(Susceptible.count + Infected.count + Recovered.count + Escape.count)}\n")
        stepCount += 1
        
             
if __name__ == "__main__":
    main() 