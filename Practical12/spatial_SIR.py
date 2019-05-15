# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:47:56 2019

@author: jxm72
"""

import numpy as np 
import matplotlib . pyplot as plt
population = np. zeros ( (100 , 100) )
#randomly select one infected people
outbreak = np.random.choice(range(100) ,2) 
print(outbreak)
population[outbreak[0],outbreak[1]] = 1
plt.figure( figsize =(6 ,4) , dpi=150) 
plt.imshow( population , cmap='viridis' , interpolation='nearest')
infectedplace=np.where(population==1)
xx=infectedplace[0]
yy=infectedplace[1]
for j in range(100):
    for i in range(len(xx)):        
        x=xx[i]
        y=yy[i]
        #find the neighbour 
        for xneighbour in range(x-1,x+2):
            for yneighbour in range(y-1,y+2):
                #the neighbour is not itself
                if (xneighbour,yneighbour) != (x,y):
                    #the neighbour don't exceed the range 
                    if xneighbour != -1 and yneighbour != -1 and xneighbour!=100 and yneighbour!=100:
                        #from the susceptible people choose whether they are infected
                        if population[xneighbour,yneighbour]==0:
                            population[xneighbour,yneighbour]=np.random.choice(range(2),1,p=[0.7,0.3])
                            #the susceptible people are infected
                            if population[xneighbour,yneighbour]==1:
                                xneighbour=np.array([xneighbour])
                                yneighbour=np.array(yneighbour) 
                                #append the newly infected people's location to the array so that it could enter the next loop
                                xx=np.append(xx,xneighbour)
                                yy=np.append(yy,yneighbour)
                        if population[xneighbour,yneighbour]==1:
                            #randomly select people to recover; recovered people were assigned number 2 while unrecovered were still 1
                            population[xneighbour,yneighbour]=np.random.choice(range(1,3),1,p=[0.95,0.05])
                                         
    #print the figure when it runs 0,10,50,100 times
    if j in [0,10,50,100]:
        plt.figure( figsize =(6 ,4) , dpi=150) 
        plt.imshow( population , cmap='viridis' , interpolation='nearest')
            
    
    
