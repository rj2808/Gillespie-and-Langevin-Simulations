from random import random
import math
import matplotlib.pyplot as plt
from numpy import *
# Code to be used for
__author__ = 'Rakshit'
# Defining a Class of Simulations to make life easier
class Gillespie :
        time,molA, molB = [], [], []
        time  += [0]

        	# Applying the Stocastic Algorithm
    		# For the Reaction A + B -> A
            # Solved the same problem using arrays
        def Algorithm_for_Simulation(self,Rate) :
            plt.ion()
            plt.axis([0,12,0,self.molA[0]])
            i = 0
            while 1 :

                propensity = self.molA[i]*self.molB[0]*Rate
                # Ending the Loop as soon as molA reaches zero
                if propensity <= 0 :
                    return 0
                # Applying Gillespie Algorithm
                self.molA += [self.molA[i] - 1]
                # Time is an exponential random variable
                self.time += [self.time[i] + random.exponential(1/propensity)]
                i = i +1
                print(self.time[i], self.molA[i])


        # Running the Algorithm
        def run(self, a, b, Rate):
            # Setup for the simulations
            self.molA  += [a]
            self.molB  += [b]

            self.Algorithm_for_Simulation(Rate)
            plt.plot(self.time,self.molA)
G = Gillespie()
G.run(20000,1,1)
plt.show()
plt.pause(2**31-1)
