# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:28:35 2019

@author: wjx
"""

word=input('Give me a string of words:')
Word=word.split()#convert the string into list
r_word=[x[::-1] for x in Word]#reverse every word in the list
s_word=sorted(r_word,reverse=True)#sorted the word accoding to the first letter in reverse order
print(s_word)

