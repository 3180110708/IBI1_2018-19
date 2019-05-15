# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:07:03 2019

@author: jxm72
"""
import numpy as np
import os
import matplotlib.pyplot as plt
import xml.dom.minidom

#os.chdir("C:\Users\jxm72\Desktop\semester2\IBI1\GitHub\IBI1_2018-19\Practical13\runPredatorPrey.py")
def xml_to_cps():
    import os
    import xml.dom.minidom
    
    # first, convert xml to cps 
    os.system("CopasiSE.exe -i predator-prey.xml -s predator-prey.cps")
    
    # now comes the painful part. Just copy and paste this ok
    
    cpsTree = xml.dom.minidom.parse("predator-prey.cps")
    cpsCollection = cpsTree.documentElement
    
    reportFile = xml.dom.minidom.parse("report_ref.xml")
    reportLine = reportFile.documentElement
    
    tasks = cpsCollection.getElementsByTagName("Task")
    for task in tasks:
        if task.getAttribute("name")=="Time-Course":
            task.setAttribute("scheduled","true")
            task.insertBefore(reportLine,task.childNodes[0])
            break
        
    
    for taskDetails in task.childNodes:
        if taskDetails.nodeType ==1:
            if taskDetails.nodeName == "Problem":
                problem = taskDetails
                
    for param in problem.childNodes:
        if param.nodeType ==1:
            if param.getAttribute("name")=="StepNumber":
                param.setAttribute("value","200")
            if param.getAttribute("name")=="StepSize":
                param.setAttribute("value","1")
            if param.getAttribute("name")=="Duration":
                param.setAttribute("value","200")
           
            
    report18 = xml.dom.minidom.parse("report18.xml")
    report = report18.documentElement
    
    listOfReports  =  cpsCollection.getElementsByTagName("ListOfReports")[0]
    listOfReports.appendChild(report)
    
    cpsFile = open("predator-prey.cps","w",encoding='utf-8')
    cpsTree.writexml(cpsFile)
    cpsFile.close()
    
        
        
#plot the conten of csv        
def plotcsv():
    #transfer a new xml file to cps
    xml_to_cps() 
    #run the copasi file
    os.system("CopasiSE.exe predator-prey.cps")  
    #read the content of csv file
    file=open('modelResults.csv','r')
    names=np.array(['Time','[A]','[B]'])
    data=np.array([])
    datalist=[]
    for line in file:
       # print(line)    
        lines=line.split(',')    
        datalist.append(lines)
        
    del datalist[0]
        
    data=np.array(datalist)    
    results=data.astype(np.float)
    
    #plot predator and prey against time
    plt.plot(results[:,1])
    plt.plot(results[:,2])
    plt.title('Time course')
    plt.ylabel('population size')
    plt.xlabel('time')
    plt.legend((('Predator (b='+str(k_predator_breeds)+', d='+str(k_predator_dies)+')'),('prey (b='+str(k_prey_breeds)+', d='+str(k_prey_dies)+')')))
    plt.show()
    #plot predator against prey    
    plt.plot(results[:,1],results[:,2]) 
    plt.title('Limit cycle')
    plt.ylabel('prey population')
    plt.xlabel('predator population')
    plt.show()
    file.close()
    return results[:,1],results[:,2]

def editxml(): 
    #open and parse the xml file, build a tree
    fileName='predator-prey.xml'
    Tree = xml.dom.minidom.parse(fileName) 
    obo=Tree.documentElement
    term=obo.getElementsByTagName('listOfParameters')[0]    
    parameter=term.getElementsByTagName('parameter')
    #edit the four parameters
    for t in parameter:
        if t.getAttribute('name')=='k_predator_dies':                   
            t.setAttribute('value',str(k_predator_dies))                       
        if t.getAttribute('name')=='k_predator_breeds': 
            t.setAttribute('value',str(k_predator_breeds))
        if t.getAttribute('name')=='k_prey_breeds': 
            t.setAttribute('value',str(k_prey_breeds))
        if t.getAttribute('name')=='k_prey_dies': 
            t.setAttribute('value',str(k_prey_dies))
    #save the change to xml file
    cpsFile = open("predator-prey.xml","w",encoding='utf-8')
    Tree.writexml(cpsFile)
    cpsFile.close()
    


k_predator_dies=0.4
k_predator_breeds=0.02
k_prey_breeds=0.1
k_prey_dies=0.02
editxml()
plotcsv()



#simulate multiple times and visulise the result
for i in range(10):
    k_predator_dies=np.random.sample()
    k_predator_breeds=np.random.sample()
    k_prey_breeds=np.random.sample()
    k_prey_dies=np.random.sample()
    editxml()    
    list=plotcsv()
    #print the max number of predator and prey during the simulation
    print('the max number of predator is:',np.amax(list[0]))
    print('the max number of predator is:',np.amax(list[1]))
    





