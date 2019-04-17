# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 18:24:32 2019

@author: jxm72
"""

import itertools
recursion=0
number=input("Please input numbers to compute 24:(use ',' to devide them)")
num=number.split(',')
num=list(map(int,num))
permutation=list(itertools.permutations(num))#get all the permutations

oplist=['+','-','*','/']

permutation2=list(itertools.permutations(oplist,len(num)-1))
combination=list(itertools.combinations(num,2))


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
        
        
        
def sort(N):
    if len(N)<2:
        return N[:]
    elif len(N)%2==0:
        lis=[N[i:i+2] for i in range(0,len(N),2)]
        return lis
    elif len(N)%2==1:
        lis=[N[i:i+2] for i in range(1,len(N),2)]
        lis.append([N[0]])
        return lis


def compute(N,op):
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
    





for i in range(len(permutation)):
    #print(permutation[i])
   # num=sort(permutation[i])
    num=permutation[i]
    print(num)
    while p24(num)==False:
        for j in range(len(num)):
            for op in ['+','-','*','/']:
                print(num[j])
                num=(compute(num,op),)+num
                
                print(num)
                        
                    
                
               