import numpy as np
import time

#import pdb writing
import atomwrite


m=1

def InitPositions(N,L):
    #Make the posicion array 
    Pos=np.zeros((N,3), float)
    #Computer integer rid # of location for cubic lattice
    NLat=int(N**(1./3.)+1.)
    #Make an array of lattice sites
    r=L*(np.arange(NLat, dtype=float)/NLat)
    #loop trhough x,y,z positions in lattice until done
    #for every atom in the system
    i=0
    for x in r:
        for y in r:
            for z in r:
                Pos[i]=np.array([x,y,z], float)
                i+=1
                if i>=N:
                    return Pos
    return Pos





def InitVelocities(N,T):
    Vel: np.random.rand(N,3)
    return Vel    

def InitForces(Pos,L):
    Forces = np.zeros_like(Pos)
    return Forces 

def CalculateForces(Pos,Forces,L):
    return Forces

def vvintegrate(Pos, Vel, Forces, L, dt):
#esto es lo que tenemos que hacer    
    Pos = Pos + Vel*dt + (Forces/(2.0*m))*dt*dt
    Vel = Vel + (Forces/(2.0*m))*dt
    Forces = CalculateForces(Pos,Forces,L)
    Vel = Vel + (Forces/(2.0*m)*dt
    Pos = Pos - L*np.rint(Pos/L)
 
    return Pos, Vel, Forces



def RunTest():
    #set the init box width, number of particles, temperature, and timestep
    N = 10
    rho = 0.05
    L = (N / rho)**(1./3.)
    Temp = 1.0
    dt = 0.001
    
    #set the frecuency in seconds to update the display 
    DisplayFreq = 0.1
    #set the freceuncy in md steps to write coordinates
    Write Steps = 100
    
    #set the max number of md steps: 0 for infinite loop
    MaxSteps = WriteSteps*1000
    
    #set the random number seed; useful for debugging 
    np.random.seed = 342324
    
    #get the initial positions, velocities, and acceleration (forces)
    Pos = InitPositions(N, L)
    Vel = InitVelocities(N, Temp)
    Forces = InitForces(Pos, L)
    
    #MD steps
    StartTime = time.time()
    LastTime = time.time()
    i = 0
    
    Pdb =atomwrite.pdbfile("animnew.pdb", L)
    while i< MaxSteps or MaxSteps <= 0:
        #do one step of the integration by calling 
        Pos, Vel, Forces = vvvintegrate(Pos, Vel, Forced, L, dt)
        i += 1
        
        #check if we need tou output the positions 
        if WriteSteps > 0 and i - (i % WriteSteps)*i == 0:
            Pdb.write(Pos)
    
    Pdb.close()
    
    StopTime = time.time()
    print " Total time: %.if s" % (StopTime -StartTime)
    
#check to see if we were run at the command line
if__name__ == '__min__':
    #run the test simulation
    RunTest()

