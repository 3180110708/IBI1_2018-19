# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:03:15 2019

@author: wjx
"""

import matplotlib.pyplot as plt
DNA=input('give me a sequence of DNA:')
dna=list(DNA)#convert to list
#count the number for every nucleotide
a=dna.count('A')
c=dna.count('C')
g=dna.count('G')
t=dna.count('T')
#creat a dictionary
dict={'A': a, 'G': g, 'C': c, 'T': t}
print(dict)

#creat pie
labels='A','G','C','T'
sizes=[a,g,c,t]
fig,plot=plt.subplots()
plot.pie(sizes,labels=labels,autopct='%1.1f%%')
plot.axis('equal')
plot.set_title('pie of the four nucleotides')

plt.show()