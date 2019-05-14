import xml.dom.minidom
import pandas as pd

fileName='go_obo.xml'
DOMTree = xml.dom.minidom.parse(fileName) 
obo = DOMTree.documentElement
go = obo.getElementsByTagName('term')

termlist=[]
idlist=[]
namelist=[]
definition=[]
numberofchild=[]
#define function to count the number of childnodes
def Child(id, resultSet):
    #we need to find childnodes from all the terms, but not only the ones that are related to autophagosome
    for t in go:
        parents = t.getElementsByTagName('is_a')
        geneid = t.getElementsByTagName('id')[0].childNodes[0].data
        for parent in parents:
            #get the id of child by finding its parent
            if parent.childNodes[0].data == id:
                resultSet.add(geneid)
                #iterate until there is no childnodes for this id
                Child(geneid, resultSet)
#get the terms that has 'autophagosome' in its definition
for term in go:
    description=term.getElementsByTagName('defstr')[0].childNodes[0].data
    if 'autophagosome' in description:
        termlist.append(term)
#collect the data       
for term in termlist:
    id=term.getElementsByTagName('id')[0].childNodes[0].data
    idlist.append(id)
    namelist.append(term.getElementsByTagName('name')[0].childNodes[0].data)
    definition.append(term.getElementsByTagName('defstr')[0].childNodes[0].data)
    resultSet = set()
    Child(id, resultSet)
    print(id, len(resultSet))
    numberofchild.append(len(resultSet))
#make a dataframe
data={'id':[idlist],'name':[namelist],'definition':[definition],'childnodes':[numberofchild]}  
df=pd.DataFrame(data)    
df.to_excel('autophagosome.xlsx',index=False)
print(df)    