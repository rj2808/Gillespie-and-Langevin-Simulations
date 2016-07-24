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
            while i <= self.n :
                a_1 = self.Kp*self.R[i]
                a_2 = self.Kr*self.V
                a_3 = self.Kmi*self.V
                a_4 = self.Kt*self.
