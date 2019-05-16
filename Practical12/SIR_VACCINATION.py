# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:06:54 2019

@author: jxm72
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
for j in range(11):
    N=10000
    beta=0.3
    gamma=0.05
    infected=1
    susceptible=9999
    recovered=0
    #the different propotion of people get vaccinated
    vaccination=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    track=np.array((infected,susceptible,recovered))
    for i in range(1000):      
        propotion=beta*(infected/N)

        getinfected=np.random.choice(range(2),susceptible-int(susceptible*vaccination[j]),p=[1-propotion,propotion])
        getrecovered=np.random.choice(range(2),infected,p=[1-gamma,gamma])
        getinfected=sum(getinfected)
        getrecovered=sum(getrecovered)
        infected=infected+getinfected-getrecovered
        susceptible=susceptible-getinfected
        recovered=recovered+getrecovered
        
        track1=np.array((infected,susceptible,recovered))
        track=np.append(track,track1)
    
    
    x=[track[i] for i in range(0,len(track),3)]
    plt.ylabel('number of people')
    plt.xlabel('time')
    y_pos=np.arange(1000)
    plt.plot(x)
    plt.legend(['0','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'])
    plt.title('SIR model')
    
plt.savefig ("SIR_vaccination.png" ,type="png")
#plt.show()

