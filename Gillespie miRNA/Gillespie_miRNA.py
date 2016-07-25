from random import random
import math
import matplotlib.pyplot as plt
from numpy import *
# Code to be used for
__author__ = 'Rakshit'
# Defining a Class of Simulations to make life easier
class Gillespie :
        time,molR, molP, molMi = [], [], [], []
        Kp, Kmi, Kt, Yr, Yp, Ymi, V, n = 0;
        time  += [0]
        def Algorithm_for_Simulation(self, Rate) :
            i = 0
            plt.ion()
            while i <= self.n :
                # Defining various propensities
                # Clearly these depend on the system volume as it evolves
                a_1 = self.Kp*self.molR[i]
                a_2 = self.Kr*self.V
                a_3 = self.Kmi*self.V
                a_4 = self.Kt*self.molR[i]*self.molMi[i]
                a_5 = self.Yr*self.molR[i]
                a_6 = self.Ymi*self.molMi[i]
                a_7 = self.Yp.self.molP[i]
                propensity = a_1 + a_2 + a_3 + a_4 _a_5 + a_6 + a_7
                # Calculating factors for selecting which reactions to occur
                # Calculating sort of probablities by which reactions should occur
                p1 = a_1/propensity
                p2 = p1 + a_2/propensity
                p3 = p2 + a_3/propensity
                p4 = p3 + a_4/propensity
                p5 = p4 + a_5/propensity
                p6 = p5 + a_6/propensity
                p7 = p6 + a_7/propensity
                print(p7)
                # An exponential time variable to govern when will the next reaction occur
                self.time += [self.time[i] + random.exponential(1/propensity)]
                a = random.random()

                # Selecting which reaction should occur

                if p1 <= a < p2 :
                    molP += [molP[i] + 1]
                    molR += [molR[i]]
                    molMi += [molMi[i]]
                if p2 <= a < p3 :
                    molR += [molR[i] + 1]
                    molMi += [molMi[i]]
                    molP += [molP[i]]
                if p3 <= a < p4 :
                    molMi += [molMi[i] + 1]
                    molP += [molP[i]]
                    molR += [molR[i]]
                if p4 <= a < p5 :
                    molMi += []
