# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 11:06:46 2019

@author: jxm72
"""

count=13
n=1750
a='1750 is 2**'
while n!=0:
    if n-2**count<0:
        count=count-1
        continue
    if n-2**count>0:
        a=a+str(count)+'+2**'
        n=n-2**count
        continue
    if n-2**count==0:
        a=a+str(count)
        break
print(a)
    