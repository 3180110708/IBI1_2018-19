from fractions import Fraction
i=1
#if the number does not meet the standard, the user is asked to input again
while i!=0:
    i=0
    data=input("Please input numbers to computer 24:(use ',' to divide them)\n")
    numlist=data.split(',')
    #transfer the string to float so that it could be calculated directly; store the integers in a list
    num=list(map(float,numlist)) 
    #check if the numbers meet the stansard
    for number in num:
        #the number should be ranging from 1 to 23
        if number>23 or number<1 or number%1!=0:
            print('The input number must be intergers from 1 to 23')
            i=1
            break
#transfer the string to integer to avoid irrational number problem      
num=list(map(int,numlist))
#recursion times
count=0 
#l is length of num
#I don't directly use num because when there is only one element in the num the type of num is int, then len() doesn't work on int
#recurtion
def deepfirstsearch(l):
    #count the recursion times
    global count
    count+=1     
    if l==1:
        if(float(num[0])==24):
            return 1
        else:
            return 0
    
    #select two different numbers
    for i in range(0,l):       
        for j in range(i+1,l):  
            
            a=num[i]
            b=num[j]
            #for each iteration, move the last number ahead so that it won't calculate on number twice
            num[j]=num[l-1]            
            num[i]=a+b            
            #goes deep until there is only one number left
            #each time there will be one number less
            #each time try a different operator from the 6 operators below, test all arithmetic combinations
            if deepfirstsearch(l-1)==1:
                return 1            
            num[i] = a*b            
            if deepfirstsearch(l-1)==1:
                return 1  
            num[i] = a-b            
            if deepfirstsearch(l-1)==1:
                return 1             
            num[i] = b-a            
            if deepfirstsearch(l-1)==1:
                return 1 
            if a!=0:
                #if a does not equal to 0, use Fraction() to divide b by a
                #use Fraction but not '/' to avoid the problem of irrational number,that is, the imprecise float 
                num[i]=Fraction(b,a)
                if deepfirstsearch(l-1)==1: 
                    return 1 
            if b!=0:
                num[i]=Fraction(a,b)
                if deepfirstsearch(l-1)==1: 
                    return 1 
            #for each loop, backtrack the num list 
            num[i]=a
            num[j]=b
    return 0 

#test for stop condition
if deepfirstsearch(len(num))==1: 
    print('Yes')
else: 
    print('No')
print('Number of atom operations:',count)

