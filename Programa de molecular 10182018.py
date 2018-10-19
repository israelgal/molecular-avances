# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 23:05:32 2018

@author: iisra
"""

def initPositions(N, L):
    """Returns an array of initial positions of each atom,
placed on a cubic lattice for convenience.

"""






def InitVelocities(N,T):
    """Returns an initial random velocity set.
Input:
    N: number of atoms 
    T: target temperature 
Output:
    Vel: (N,J) array of atomic velocities 
"""
    Vel: np.random.rand(N,3)
    return Vel    

def InitForces(Pos,L):
    Forces = np.zeros_like(Pos)
    return Forces 

def CalculateForces(Pos,Forces,L):
    return Forces

#def vvintegrate(Pos, Vel, Forced, L, dt):
#esto es lo que tenemos que hacer    
def RunTest():
    #set the init box width, number of particles, temperature, and
    N = 10
    rho = 0.05
    L = (N / rho)**(1./3.)
    Temp = 1.0
    dt = 0.001
    
    #set the frecuency in seconds to update the display 
    DisplayFreq = 0.1
    #set the freceuncy in md steps to write coordinates
    WriteSteps = 100
    
    #set the max number of md steps: 0 for infinite loop
    MaxSteps = WriteSteps*1000
    
    #set the random number seed; useful for debugging 
    np.random.seed = 342324
    
    #get the initial positions, velocities, and acceleration (forces)
    Pos = InitPositions(N, L)
    Vel = InitVelocities(N, Temp)
    Forces = InitForces(Pos, L)
    
    StartTime = time.time()
    LastTime = time.time()
    i = 0
    
    Pdb =atomwrite.pdbfile("animnew.pdb", L)
    while i< MaxSteps or MaxSteps <= 0;
        #do one step of the integration by calling 
        Pos, Vel, Forces = vvvintegrate(Pos, Vel, Forced, L, dt)
        i += 1
        
        #check