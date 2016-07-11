import random
import math
import numpy as np
import matplotlib as plt

__author__ = 'Rakshit'

class Gillespie()
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
		def Algorithm_for_Simulation (self, Rate)
			while self.molA >= 0		# Loop Until the Value of A is zero
					propensity = (self.molA * self.molB) * rate

					if propensity == 0
							return 0
					self.molA -= 1

					self.time +=  (-1/propensity)*math.log(random.random()) # Calculating Time Increment

					print(self.time,self.molA/(self.molA +self.molB),self.molB/(self.molA + self.molB)) # Prining out the Arguements
