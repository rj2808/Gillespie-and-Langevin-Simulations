import random
import math
import numpy as np
import matplotlib as plt

__author__ = 'Rakshit'

class Gillespie :
		# Initialising the Parameters
		time,molA,molB = 0,0,0
		h,j = 0,0
		ka,kKa,kb,kKb = 0,0,0,0
		da, db = 0,0
		prop = []
		n_prop = []
		p_sum = 0

		# Applying the Stocastic Algorithm
		# For the Reaction A + B -> A
		def Algorithm_for_Simulation(self, Rate) :
			while self.molA >= 0 :
					propensity = (self.molA * self.molB) * Rate

					if propensity == 0:
						 return 0
					self.molA -= 1

					self.time +=  (-1/propensity)*math.log(random.random()) # Calculating Time Increment

					print(self.time,self.molA/(self.molA +self.molB),self.molB/(self.molA + self.molB)) # Prining out the Arguements

		# Function used to run the simulations
		def run(self,a,b,Rate) :
				self.molA = a
				self.molB = b
				self.Algorithm_for_Simulation(Rate)
G = Gillespie()
G.run(19999,1,1)
