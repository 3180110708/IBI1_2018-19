# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 11:06:46 2019

@author: wjx
"""
#find the biggest power of 2 that is smaller than n through trying power of 2 from 13 and then going down
#n substract that power of 2 and then find the biggest power of 2 that is smaller than the difference
#stop until the difference is 0
#output

#name count as the power, count down from 13
count=13
#user input a number
n=int(input())
#some unchanged things
a=str(n)+' is 2**'
#three conditions
while n!=0:
    if n-2**count<0:
        count=count-1#try a small power
    elif n-2**count>0:#that is the biggest power that smaller than n
        a=a+str(count)+'+2**'
        n=n-2**count#use the difference to continue 
    elif n-2**count==0:#means that is the last one
        a=a+str(count)
        break
print(a)#output the result
    