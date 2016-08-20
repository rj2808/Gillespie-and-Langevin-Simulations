from random import random
import math
import matplotlib.pyplot as plt
from numpy import *
# Code to be used for
__author__ = 'Rakshit'
# Defining a Class of Simulations to make life easier
class Gillespie :
        time,molR, molP, molMi = [], [], [], []
        def Algorithm_for_Simulation(self, Kr, Kmi, Kp, Kt, Yr, Ymi, Yp, V, n) :
            i = 0
            while i <= n :
            
                # Defining various propensities
                # Clearly these depend on the system volume as it evolves
                a_1 = Kp*self.molR[i]
                a_2 = Kr*V
                a_3 = Kmi*V
                a_4 = Kt*self.molR[i]*self.molMi[i]
                a_5 = Yr*self.molR[i]
                a_6 = Ymi*self.molMi[i]
                a_7 = Yp*self.molP[i]
                propensity = a_1 + a_2 + a_3 + a_4 +a_5 + a_6 + a_7
                # Calculating factors for selecting which reactions to occur
                # Calculating sort of probablities by which reactions should occur
                p1 = a_1/propensity
                p2 = p1 + a_2/propensity
                p3 = p2 + a_3/propensity
                p4 = p3 + a_4/propensity
                p5 = p4 + a_5/propensity
                p6 = p5 + a_6/propensity
                p7 = p6 + a_7/propensity
            
                # An exponential time variable to govern when will the next reaction occur
                self.time += [self.time[i] + random.exponential(1/propensity)]
                a = random.random()

                # Selecting which reaction should occur
                # Formation of protien
                if 0 <= a < p1 :
                    self.molP  += [self.molP[i] + 1]
                    self.molR  += [self.molR[i]]
                    self.molMi += [self.molMi[i]]
                # Formation of mRNA
                if p1 <= a < p2 :
                    self.molR  += [self.molR[i] + 1]
                    self.molMi += [self.molMi[i]]
                    self.molP  += [self.molP[i]]
                # Formation of miRNA
                if p2 <= a < p3 :
                    self.molMi += [self.molMi[i] + 1]
                    self.molP  += [self.molP[i]]
                    self.molR  += [self.molR[i]]
                # Regulation term
                if p3 <= a < p4 :
                    self.molMi += [self.molMi[i] - 1]
                    self.molR  += [self.molR[i] -1]
                    self.molP  += [self.molP[i]]
                # Decay of mRNA
                if p4 <= a < p5 :
                    self.molR  += [self.molR[i] -1]
                    self.molMi += [self.molMi[i]]
                    self.molP  += [self.molP[i]]
                # Decay of miRNA
                if p5 <= a < p6 :
                    self.molMi += [self.molMi[i] - 1]
                    self.molR  += [self.molR[i]]
                    self.molP  +=  [self.molP[i]]
                if p6 <= a < p7 :
                    self.molP  += [self.molP[i] -1]
                    self.molMi += [self.molMi[i]]
                    self.molR  += [self.molR[i]]
                #print(self.molMi[i])
                #print(self.time[i], self.molR[i], self.molMi[i], self.molP[i])
                i = i +1
                #print(i/n * 100)

        def run(self, R, P, Mi, Kr, Kmi, Kp, Kt, Yr, Ymi, Yp, V, n):
            # Deletition of these array is neccesary
            del self.molMi[:]
            del self.molR[:]
            del self.molP[:]
            del self.time[:]
            self.molR += [R]
            self.molP += [P]
            self.molMi += [Mi]
            self.time += [0]
            self.Algorithm_for_Simulation(Kr, Kmi, Kp, Kt, Yr, Ymi, Yp, V, n)
            # Using Subplots to display the plots

            plt.subplot(221)
            plt.plot(self.time,self.molP)
            plt.yscale('linear')
            plt.title('protien')

            plt.subplot(222)
            plt.plot(self.time,self.molMi)
            plt.yscale('linear')
            plt.title('miRNA')

            plt.subplot(223)
            plt.plot(self.time,self.molR)
            plt.yscale('linear')
            plt.title('mRNA')
            
            

G = Gillespie()
fig = plt.figure(1)
G.run(10000,10000,10000,10,10,1,.0001,.001,.001,1,1000000,100000000)
plt.savefig('(10000,10000,10000,10,10,1,.0001,.001,.001,1,1000000,10000000).png')
plt.close()
print('First Reaction set complete')


fig2 = plt.figure(2)
G.run(10000,10000,10000,10,10,1,.001,.001,.001,1,1000000,100000000)
plt.savefig('(10000,10000,10000,10,10,1,.001,.001,.001,1,1000000,10000000).png')
plt.close()
print('Both Reaction set complete')




