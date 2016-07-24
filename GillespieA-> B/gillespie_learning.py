import random 
import math

__author__ = 'joe'

class Gillespie():
	time,molA,molB = 0,0,0					# Timescale, molecule A and B
	h,j = 0,0								# Variable h and j
	ka,kKa,kb,kKb = 0,0,0,0					# Variable ka, Ka, kb, Kb
	da,db = 0,0								# Variable db, da
	props = []
	n_props = []
	p_sum = 0

	# Algorithm to simulate the reaction of molecule A and B in the system
	def system1(self,rate):
		while self.molA >= 0:				# Loop until the value of molecule A is 0
			propensity = (self.molA * self.molB) * rate	# Calculate propensity

			if propensity == 0:				# Ensure that the rate is not 0
				return 0

			self.molA -= 1 					# Decrement a molecule

			self.time += ((-1/propensity)*math.log(random.random())) # Calculate time increment

			print (self.time, self.molA/(self.molA+self.molB), self.molB/(self.molB+self.molA))

	# Algorithm to simulate the reactions of System 2
	def system2(self):
		while self.molA >0 and self.molB >0:
			r1 = self.molB * (self.kb * ( ( (self.molA**self.h)*self.kKb) / ( (self.kKa+(self.molA**self.h)) * (self.kKb+(self.molB**self.j)))))
			r2 = (self.molB * self.db)
			r3 = self.molA * (self.ka * ( ( (self.molB**self.j)*self.kKa) / ( (self.kKa+(self.molA**self.h)) * (self.kKb+(self.molB**self.j)))))
			r4 = (self.molA * self.da)

			self.props.append([r1,"r1"])
			self.props.append([r2,"r2"])
			self.props.append([r3,"r3"])
			self.props.append([r4,"r4"])

			self.props.sort()				# sort props by propensity

			self.p_sum = self.props[0][0] + self.props[1][0] + self.props[2][0] + self.props[3][0]

			self.normalise(self.props,self.p_sum)

			rand = self.p_sum*random.random()	# generate a number for pick_prop

			r = self.pick_reaction(rand, self.n_props)		# reaction picked

			if r == "r1":
				self.molB += 1
			elif r == "r2":
				self.molB -= 1
			elif r == "r3":
				self.molA += 1
			elif r == "r4":
				self.molA -= 1

			self.time += ((-1/self.p_sum)*math.log(random.random())) #timeincrement

			print (self.time, r, self.molA, self.molB)

	# Function to pick which reaction has occoured
	def pick_reaction(self,rand,prop_list):
		for q in range(len(prop_list)):			# loop through the first 3
			if rand <= prop_list[q][0]:
				return prop_list[q][1]
			else: prop_list[len(prop_list)-1][1]	# return last

	def normalise(self, props, p_sum):
		for p in range(len(props)):
			self.n_props.append([(props[p][0]/p_sum),props[p][1]])

	# Setup function
	# Takes an inut of parameter values and sets up the 
	# simulation accourdingly.
	def run(self,a,b,rate,sys,system2_v):
		self.molA = a
		self.molB = b

		if sys == 'sys1':				# Run system 1
			self.system1(rate)
		elif sys == 'sys2':				# Run system 2
			if system2_v != []:
				self.h = system2_v[0]	#h
				self.j = system2_v[1]	#j
				self.ka = system2_v[2]	#ka
				self.kKa = system2_v[3]	#kKa
				self.kb = system2_v[4]	#kb
				self.kKb = system2_v[5]	#kKb
				self.da = system2_v[6]	#da
				self.db = system2_v[7]	#db
			self.system2()
		else:
			return 0

# To change systems, comment either line 101 OR 102 respectively
G = Gillespie()
G.run(19999,1,1,'sys1',[])
# G.run(200, 100, 0,'sys2',[2, -2, 900, 800, 200, 2, 20, 3])
#     mola molb rate      h  j  ka Ka kb Kb da   db