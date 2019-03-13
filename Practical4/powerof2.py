# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:10:56 2019

@author: jxm72
"""

#find the power of 2 that is cloest to n
#the use the difference value of n and the power of 2 calculate again until n=0





while 1==1:
    b=0
    n=123
    if (n-2**b)>0:
        b=b+1
        n=n
    elif (n-2**b)<0:
        b=b-1
        print(b)
        n=n-2**(b-1)
            
    elif (n-2**b)==0:
        print(b)
        break
    
    
   
n=123
b=0
if (n-2**b)>0:
    b=b+1
elif (n-2**b)<0:
    while (n-2**b)<0:
        b=b-1
        print(b)
        n=n-2**b
        if n=0:
            break 

        
    
    
    
    
    
    
