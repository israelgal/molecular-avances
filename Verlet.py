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
    N= len(Pos)
    Forces.fill(0.)
    rc2=36.
    A=48.
    B=24.
    for i in range(N-1):
        Pos_i=Pos[i]
        for j in range(i+1,N):
            Pos_j=Pos[j]
            rij=Pos_i-Pos[j]
            d2=np.sum(rij*rij)
            if (d2<rc2):
                id2=1./d2
                id6=id2*id2*id2
                id12=id6*id6
                Fij=((A*id12+B*id6)*rij)
                Forces[i]=Forces[i]+Fij
                Forces[j]=Forces[j]-Fij

    return Forces

def CalculateForcesR(Pos,Forces,L):
    N= len(Pos)
    NLat=int(N**(1./3.)+1.)
    r=L*(np.arange(NLat,dtype=float)/NLat - 0.5)
    r_eq=r[1]-r[0]
    Forces.fill(0.)
    rc2=2.*L
    k=-1.
    for i in range(N-1):
        Pos_i=Pos[i]
        for j in range(i+1,N):
            Pos_j=Pos[j]
            rij=Pos_i-Pos[j]
            d2=np.sum(rij*rij)
            if (d2<rc2):
                Fij=-k*(np.abs(rij)-r_eq)*rij/d2
                Forces[i]=Forces[i]+Fij
                Forces[j]=Forces[j]-Fij

    return Forces


def vvintegrate(Pos,Vel,Forces,L,dt):
    Pos = Pos+(Vel*dt)+((Forces/2.*m)*dt**2)
    Vel = Vel+(Forces/2.*m)*dt
    Forces = CalculateForcesR(Pos,Forces,L)
    Vel = Vel+(Forces/2.*m)*dt
    Vel=np.multiply(Vel,np.ones_like(Vel)-2*np.rint(np.absolute(Pos)/L))

    return Pos,Vel,Forces

def RunTest():
    N=27
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
