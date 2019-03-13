# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:10:56 2019

@author: jxm72
"""

#make a list 
#if the number is the cloest 


b=13
n=934
count=[]
while 1==1:
    
    
    if (n-2**b)<0:
        b=b-1
    elif (n-2**b)>0:
        count.append(b)
        n=n-2**(b)
        continue   
    elif (n-2**b)==0:
        count.append(b)
        break
   
print(count)
print(len(count))
for i in (0,len(count)-1):
    print('2019','is','2**',str(count[i]),'+')

        
    
    
    
    
    
    
