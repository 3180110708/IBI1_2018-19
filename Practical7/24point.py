# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:01:28 2019

@author: jxm72
"""
import itertools
recursion=0
number=input("Please input numbers to compute 24:(use ',' to devide them)")
num=number.split(',')
num=list(map(int,num))

#print(num)
J=False
permutation=list(itertools.permutations(num))
print(permutation[1])

def multiply(n):
    total = 1
    for i in range(0, len(n)):
        total *= n[i]
      
    return total

def p24(lis):
    if len(lis)==1:
        if lis[0]==24:
            return True
        else:
            return False

def sort(N):
    if len(N)<2:
        return N[:]
    elif len(N)%2==0:
        lis=[N[i:i+2] for i in range(0,len(N),2)]
        return lis
    elif len(N)%2==1:
        lis=[N[i:i+2] for i in range(1,len(N),2)]
        lis.append([N[0]])
        return lis

    
def judge(num):
    J=False
    for i in range(len(num)):
        
        #print(num[i])
        if num[i]%24==0 or 24%num[i]==0:
            print('Yes')
            J=True
            break
        
    return J
            
def calculate(lis,op):
    result=[]
    if op=='+':
        #print(sum(lis))
        result=sum(lis)
    if op=='*':
        result.append(multiply(lis))
        
    #print(result)
            
    return result            


    



for number in num:
    if int(number)>24:
        print('The input number must be integers from 1 to 23')
        break
    elif int(number) in [1,2,3,4,6,8,12]:
        print('Yes')
        break
        
    else:
        while J==False:
            for tup in permutation:
                num=sort(tup)
            #print(num)
                list2=[]
                for i in range(len(num)):    
                #print(num[i])
                    list2.append(calculate(num[i],'+'))         
                    print(list2)
                    recursion=recursion+1
                #for i in range(len(list2)):
                for i in list2:
                    recursion=recursion+1
                    if i%24==0 or 24%i==0:
                        print('Yes')
                        J=True
                        break
                    else:
                        num=list2
            if J==False:
                while J==False:
                    num=sort(num)
            #print(num)
                    list2=[]
                    for i in range(len(num)):    
                #print(num[i])
                        list2.append(calculate(num[i],'*'))         
                        print(list2)
                        recursion=recursion+1
                #for i in range(len(list2)):
                    for i in list2:
                        recursion=recursion+1
                        if i%24==0 or 24%i==0:
                             print('Yes')
                             J=True
                             break
                        else:
                             num=list2
                    #print(num)
                
                    #print(num)
                    
                    
        
            
               
            break
          
           
print(recursion)           

#        list1=sort(num)
#        print(list1)
#        list2=judge(list1)
#        print(list2)
#        list3=calculate(list2,'+')
#        print(list3)
#        
        
        
        