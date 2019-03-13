# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:21:56 2019

@author: jxm72
"""

a = 923
b = 923923
if b % 7 == 0:
    print('b can be devided by 7')
c = b/7
d = c/11
e = d/13
if e >a:
    print('e is greater')
elif e<a:
    print('a is greater')
else:
    print('a equals to e')
    
    
    
    
x = True 
y = False
z = x and not y or y and not x
print(x!=y and z==True)
w = x!=y
print(w==z)