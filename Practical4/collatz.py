# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:43:13 2019

@author: jxm72
"""

#judge whether n is even or odd using n%2
#if even, multiple 3 and plus 1; if odd, divide by 2
#when n==1, stop
n=int(input())
while n!=1:
    if n%2==0:
        n=n/2
        print(n)
    elif n%2==1:
        n=n*3+1
        print(n)
    else:
        print('n is not an integer')