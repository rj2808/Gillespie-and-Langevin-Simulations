import random
import math
import stochpy

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
		def Algorithm_for (self, Rate)
			while self.molA >= 0		# Loop Until the Value of A is zero
					propensity = (self.molA * self.molB) * rate

					if propensity == 0
							return 0
					self.molA -= 1

					self.time +=  



