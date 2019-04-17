# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:11:23 2019

@author: jxm72
"""
from Bio.SubsMat import MatrixInfo 
human='MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK'
mouse='MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK'
random='WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL'

#get a dictionary of blosum62 from biopython
blosum62=MatrixInfo.blosum62
keys=list(blosum62.keys())
values=list(blosum62.values())
humanl=list(human)
mousel=list(mouse)
randoml=list(random)

#match the keys with values
def blosum(a,b): 
    if (a,b) in keys:
        #print(1)
        index=keys.index((a,b))
        score=values[index]
        #print(type(score))
    elif (b,a) in keys:
        index=keys.index((b,a))
        score=values[index]
        #print(score)    
    return score

#add the scores and percentage
def blosum2(a,b):
    scor=0
    per=0
    for i in range(len(human)):
        score=blosum(a[i],b[i])
        if a[i]==b[i]:
            per+=1
        perc=(per/len(humanl))*100
        scor+=score
    distance = 0		#set initial distance as zero
    for i in range(len(human)):	#compare each amino acid
          if a[i]!=b[i]:  	
                distance += 1	#add a score 1 if amino acids are different
    return scor,perc,distance
        
pair1=list(blosum2(humanl,mousel))        
pair2=list(blosum2(humanl,randoml))
pair3=list(blosum2(mousel,randoml))

print('the scores for human+mouse, human+random, random+mouse are',pair1[0],',',pair2[0],',',pair3[0])
print('the identity percentages for human+mouse, human+random, random+mouse are',pair1[1],'%',',',pair2[1],'%',',',pair3[1],'%')
print('the distance for human+mouse, human+random, random+mouse are',pair1[2],',',pair2[2],',',pair3[2])

#make a blast like sequence
def blastlike(a,b):
    if a==b:
        print(a,'--',b)
    elif (a,b) in keys:
        if values[keys.index((a,b))]>=0:
            print(a,'  ',b,'+')
        else:
            print(a,'  ',b)        
    elif (b,a) in keys:
        if values[keys.index((b,a))]>=0:
            print(a,'  ',b,'+')
        else:
            print(a,'  ',b)        
for i in range(len(human)):
    blastlike(human[i],mouse[i])
    
    
    
    
    
#scor=0
#per=0
#for i in range(len(humanl)):    
#    score=blosum(humanl[i],mousel[i])    
#    if humanl[i]==mousel[i]:
#        per+=1    
#    perc1=(per/len(humanl))*100
#    scor=scor+score
#pair1=scor
#per=0
#scor=0
#for i in range(len(humanl)):    
#    score=blosum(humanl[i],randoml[i]) 
#    #print(score)
#    #print(scor)
#    if humanl[i]==randoml[i]:
#        per+=1
#    perc2=(per/len(humanl))*100
#    
#    scor=scor+score       
#pair2=scor
#per=0
#scor=0
#for i in range(len(mousel)):    
#    score=blosum(randoml[i],mousel[i]) 
#    #print(score)
#    #print(scor)
#    if randoml[i]==mousel[i]:
#        per+=1
#    perc3=(per/len(humanl))*100
#    scor=scor+score
#pair3=scor
