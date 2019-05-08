# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:06:54 2019

@author: jxm72
"""

import numpy as np
import matplotlib.pyplot as plt

for j in range(10):
    N=10000
    infected=1
    susceptible=9999
    recovered=0
    vaccination=[1000,2000,3000,4000,5000,6000,7000,8000,9000,9999]
    track=np.array((infected,susceptible,recovered))
    for i in range(1000):      
        propotion=0.3*(infected/10000)
        getinfected=np.random.choice(range(2),susceptible-vaccination[j],p=[1-propotion,propotion])
        getrecovered=np.random.choice(range(2),infected,p=[0.95,0.05])
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
    plt.legend(['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%',])
    plt.title('SIR model')
    

