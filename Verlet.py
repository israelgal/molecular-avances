import numpy as np
import time
import atomwrite

m=1.

T=1.

def InitPositions(N,L):
    Pos=np.zeros((N,3), float)
    NLat=int(N**(1./3.))
    r=L*(np.arange(NLat, dtype=float)/NLat-0.5)
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
    Vel=np.random.rand(N,3)
    return Vel

def InitForces(Pos,L):
    Forces=np.zeros_like(Pos)
    return Forces

def CalculateForces(Pos,Forces,L):
    return Forces

def vvintegrate(Pos,Vel,Forces,L,dt):
    Pos = Pos+(Vel*dt)+((Forces/2.*m)*dt**2)
    Vel = Vel+(Forces/2.*m)*dt
    Forces = CalculateForces(Pos,Forces,L)
    Vel = Vel+(Forces/2.*m)*dt
    Vel=np.multiply(Vel,np.ones_like(Vel)-2*np.rint(np.absolute(Pos)/L))

    return Pos,Vel,Forces

def RunTest():
    N=10
    rho=.05
    L=(N/rho)**(1./3.)
    Temp=1.0
    dt=0.001
    
    DisplayFrc=.1
    WriteSteps=100
    
    MaxSteps=WriteSteps*1000
    
    np.random.seed=342324
    
    Pos=InitPositions(N,L)
    Vel=InitVelocities(N,Temp)
    Forces=InitForces(Pos,L)
    
    StartTime=time.time()
    LastTime=time.time()
    i=0
    
    Pdb=atomwrite.pdbfile("animnew.pdb",L)
    while i<MaxSteps or MaxSteps<=0:
        Pos,Vel,Forces=vvintegrate(Pos,Vel,Forces,L,dt)
        i+=1
        
        if WriteSteps>0 and i-(i % WriteSteps)*i==0:
            Pdb.write(Pos)
    Pdb.close()
    
    StopTime=time.time()
    print ("Total time: %.1f s" % (StopTime - StartTime))

if __name__ == '__main__':
    RunTest()
