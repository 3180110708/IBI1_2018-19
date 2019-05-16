
human='MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK'
mouse='MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK'
random='WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL'
l=len(human)
#get a dictionary of blosum62 
file=open('blosum62.txt','r')
blosum62=eval(file.read())
keys=list(blosum62.keys())
values=list(blosum62.values())
humanl=list(human)
mousel=list(mouse)
randoml=list(random)

#match the keys with values to get the score
def blosum(a,b): 
    if (a,b) in keys:
        index=keys.index((a,b))
    #the order of the pair is considered
    else:
        index=keys.index((b,a))
    score=values[index]
    return score

#sum up the scores and identical percentage
def blosum2(a,b):
    scor=0
    per=0
    #sum the score
    for i in range(len(a)):
        score=blosum(a[i],b[i])
        #calculate the identical amino acid
        if a[i]==b[i]:
            per+=1
        perc=(per/len(a))*100
        scor+=score
    #calculate the distance between 2 protein sequence
    distance = 0		#set initial distance as zero
    for i in range(len(human)):	#compare each amino acid
          if a[i]!=b[i]:  	
                distance += 1	#add a score 1 if amino acids are different
    return scor,perc,distance   #get a list of score,identical percentage, distance

        
pair1=list(blosum2(humanl,mousel))        
pair2=list(blosum2(humanl,randoml))
pair3=list(blosum2(mousel,randoml))

print('the scores for human+mouse, human+random, random+mouse are',pair1[0],',',pair2[0],',',pair3[0],', respectively')
print('the identity percentages for human+mouse, human+random, random+mouse are',pair1[1],'%',',',pair2[1],'%',',',pair3[1],'%',', respectively')
print('the distance for human+mouse, human+random, random+mouse are',pair1[2],',',pair2[2],',',pair3[2],', respectively')
print('the normalised BLOSUM score for human+mouse, human+random, random+mouse are:',pair1[0]/l,',',pair2[0]/l,',',pair3[0]/l,', respectively \n')

#below is the 'bonus' assignment:)
#make a blast like sequence
def blastlike(a,b):
    line=[]
    line1=[]        
    for i in range(len(a)):
        if a[i]==b[i]:
            line.append(i)
        elif (a[i],b[i]) in keys:
            if values[keys.index((a[i],b[i]))]>=0:
                line1.append(i)
        elif (b[i],a[i]) in keys:
            if values[keys.index((b[i],a[i]))]>=0:
                line1.append(i)  
    #return line,line1         
    result=(line,line1)
    
    line2=['']*len(a)
    for i in range(len(a)):        
        if i in result[0]:
            line2[i]=a[i]
        elif i in result[1]:
            line2[i]='+'
        else:
            line2[i]=' '    
    print(''.join(a[0:80]),'...')
    print(''.join(line2[0:80]))
    print(''.join(b[0:80]),'...','\n')       
print('human & mouse:')
blastlike(humanl,mousel)
print('human & random:')
blastlike(humanl,randoml)
print('mouse & random:')
blastlike(mousel,randoml)   
    
    
    
    
 