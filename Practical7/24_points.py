# -*- coding: utf-8 -*-
"""
Created on Mon May 13 13:25:23 2019

@author: jxm72
"""
from fractions import Fraction
i = 1
#if the number does not meet the standard, the user is asked to input again
while i!=0:
    i=0
    data=input('Please input numbers to computer 24:(use \',\' to divide them)\n')
    numlist=data.split(',')
    num = list(map(int,numlist)) 
    for number in num:
        #the number should be ranging from 1 to 23
        if number>23 or number<1:
            print('The input number must be intergers from 1 to 23')
            i=1
        #the number should not be repetitive
        if num.count(number)>1:
            print('You should not input repetitive number')
            i=1
            break
#transfer the string to integer so that it could be calculated directly; store the integers in a list
#recursion times
count = 0 
#n is len(num) 
def deepfirstsearch(n):    
    global count
    count = count +1    
    if n == 1:
        if(float(num[0])==24):
            return 1
        else:
            return 0
    #select two different numbers
    for i in range(0,n):
        for j in range(i+1,n):            
            a = num[i]
            b = num[j]
            num[j] = num[n-1]            
            num[i] = a+b            
            #goes deep until there is only one number left
            #each time there will be one number less
            if deepfirstsearch(n-1)!=0:
                return 1            
            num[i] = a*b            
            if deepfirstsearch(n-1)!=0:
                return 1  
            num[i] = a-b            
            if deepfirstsearch(n-1)!=0:
                return 1             
            num[i] = b-a            
            if deepfirstsearch(n-1)!=0:
                return 1 
            if a!=0:
                #if a does not equal to 0, use Fraction() to divide b by a
                num[i] = Fraction(b,a)
                if(deepfirstsearch(n-1)): 
                    return 1 
            if b!=0:
                num[i] = Fraction(a,b)
                if(deepfirstsearch(n-1)): 
                    return 1 
            #for each loop, backtrack the num list 
            num[i] = a
            num[j] = b
    return 0 

if deepfirstsearch(len(num))!=0: 
    print('Yes')
else: 
    print('No')
print('Recursion times:',count)

