import numpy as np 
import matplotlib . pyplot as plt
population = np. zeros ( (100 , 100) )
#choose a person with random location to be infected
outbreak =np.random.choice(range(100) ,2) 
print(outbreak)
population[outbreak[0],outbreak[1]] = 1
beta=0.3
gamma=0.05

for j in range(101):
    #get all the location of people who are infected
    infectedIndex=np.where(population==1)
    for i in range(len(infectedIndex[0])):        
        x=infectedIndex[0][i]
        y=infectedIndex[1][i]
        
        #find the neighbours
        for xneighbour in range(x-1,x+2):
            for yneighbour in range(y-1,y+2):
                #the neighbour is not myself,not strictly necessary
                #if (xneighbour,yneighbour) != (x,y):
                #the neighbour don't fall off an edge
                if xneighbour != -1 and yneighbour != -1 and xneighbour!=100 and yneighbour!=100:
                   #from the susceptible people, not the recovered or infected people, randomly decide whether they are infected (1) or not (0)
                   if population[xneighbour,yneighbour]==0:
                       population[xneighbour,yneighbour]=np.random.choice(range(2),1,p=[1-beta,beta])
        #from all the infected people, randomly decide whether they are recovered (2) or not (1)
        population[x,y]=np.random.choice(range(1,3),1,p=[1-gamma,gamma])   
                
    #print the figure at times 0,10,50 and 100
    if j in [0,10,50,100]:
        plt.figure( figsize =(6 ,4) , dpi=150) 
        plt.imshow( population , cmap='viridis' , interpolation='nearest')
    
            
    
    
