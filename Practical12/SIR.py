# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:06:54 2019

@author: jxm72
"""

import numpy as np
import matplotlib.pyplot as plt
N=10000
beta=0.3
gamma=0.05
infected=1
susceptible=9999
recovered=0

track=np.array((susceptible,infected,recovered))

for i in range(1000):      
    propotion=beta*(infected/10000)
    getinfected=np.random.choice(range(2),susceptible,p=[1-propotion,propotion])
    getrecovered=np.random.choice(range(2),infected,p=[1-gamma,gamma])
    getinfected=sum(getinfected)
    getrecovered=sum(getrecovered)
    infected=infected+getinfected-getrecovered
    susceptible=susceptible-getinfected
    recovered=recovered+getrecovered
    #print(infected)
    track1=np.array((susceptible,infected,recovered))
    track=np.append(track,track1)
    #print(infected)

x=[track[i:i+3] for i in range(0,len(track),3)]
plt.ylabel('number of people')
plt.xlabel('time')
y_pos=np.arange(1000)
plt.plot(x)
plt.legend(['susceptible','infected','recovered'])
plt.title('SIR model')
plt.savefig ("SIR.png" ,type="png")
plt.show()  


