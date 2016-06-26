#
#
import numpy as np
import math

def Langevin_miRNA(r,p,mi,K_r,K_p,K_mi,K_t,Y_r,Y_p,Y_mi) :
    # Generating Random Numbers in order to solve Langevin Equation

     R(0) = r;
     Mi(0) = mi;
     
	 X = np.random.randn;
	 Y = np.random.randn;
	 Z = np.random.randn;
	 print X,Y,Z

	for 