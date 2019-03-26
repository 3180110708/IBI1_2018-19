# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 00:04:59 2019

@author: jxm72
"""
import matplotlib.pyplot as plt

DNA=input('give me a sequence of DNA:')
dna=list(DNA)#convert to list
nuc=['A','G','C','T']
#use a list to only collect the data of AGCT. If there is a 'N' in the string, it will not be displayed in the pie
dic=dict((x,dna.count(x)) for x in set(nuc))#creat a dictionary to count the number for every nucleotide
print(dic)

#this is used to delete the label of nucleotide that doesn't exist in the string
for x in nuc:
    if dna.count(x)==0:
        del dic[x]
        
#creat pie
labels=dic.keys()
print(dic.keys())
sizes=dic.values()
explode=[0]*len(labels)#only display the label of nucleotide that has appeared in the string
fig,plot=plt.subplots()
plot.pie(sizes,labels=labels,autopct='%1.1f%%')
plot.axis('equal')
plot.set_title('pie of the four nucleotides')

plt.show()

