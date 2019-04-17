# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 22:23:21 2019

@author: jxm72
"""
import itertools
def p24(lis):
    if len(lis)==1:
        if lis[0]==24:
            print('Yes')
            return True
        else:
            print('non')
            return False
    else:
        return False
    
def calculate(N,op):
    if len(N)==1:
        n=N
    else:
        if op=='+':
            n=N[0]+N[1]
        elif op=='*':
            n=N[0]*N[1]
        elif op=='/':
            if N[0]%N[1]==0:
                n=N[0]/N[1]
            elif N[1]%N[0]==0:
                n=N[1]/N[0]
            else:
                n=N
        elif op=='-':
            if N[0]>N[1]:
                n=N[0]-N[1]
            else:
                n=N[1]-N[0]
    
    return n


number=input("Please input numbers to compute 24:(use ',' to devide them)")
num=number.split(',')
list1=list(map(int,num)) 
list2=list1[:]      



while p24(list2)==False:
    combination=list(itertools.combinations(list2,2))
    for x in combination:
        print(x)
        p24(list2)                                                                                                                           
        list2=list1
        while len(list2)>1:
            for op in [' +','-','*','/']:               
                list2.append(calculate(x,op))
                for i in range(0,2):                
                    if x[i] in list2:
                        list2.remove(x[i])                                                           
                print(x[1])
                print(list2)
                
            
            
            
for i in list1:
    for j in list1:
        for k in oplist:
            
           
            
            
            
       e^n     
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            