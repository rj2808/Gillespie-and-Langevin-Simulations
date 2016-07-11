from random import random
import math
import numpy as np
import matplotlib.pyplot as plt

__author__ = 'Rakshit'

class Gillespie :
		# Initialising the Parameters
		time,molA,molB = 0,0,0

		# Applying the Stocastic Algorithm
		# For the Reaction A + B -> A
		def Algorithm_for_Simulation(self, Rate) :
			plt.ion()
			plt.axis([0,1.2,0,self.molA])
			while self.molA >= 0 :
					propensity = (self.molA * self.molB) * Rate

					if propensity == 0:
						 return 0
					self.molA -= 1
					# Plotting the Number of molA with time
					plt.scatter(self.time, self.molA, c=34)

					self.time +=  np.random.exponential(1/propensity)
					# Adding Exponential Solution to compare with the Deterministic solution
					y = self.molA*math.exp(-Rate*self.time)
					print(self.time,self.molA/(self.molA +self.molB),self.molB/(self.molA + self.molB)) # Prining out the Arguements
					plt.scatter(self.time, y, c=89)




		# Function used to run the simulations
		def run(self,a,b,Rate) :
				self.molA = a
				self.molB = b
				self.Algorithm_for_Simulation(Rate)
G = Gillespie()
G.run(20000,1,10)
plt.plot()
plt.show()
plt.pause(2**31-1)
