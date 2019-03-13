# What does this piece of code do?
# Answer: to find a integer between 1 and 100 that can not be exactly divided by any integer between 2 to 10

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil
#make a boolean variable
p=False
#always true
while p==False:
#if p is not false, the loop will stop
    p=True
#randomly pick a number between 1 and 100
    n = randint(1,100)
#ceil means going up for an integer,so u range from 1 to 10
    u = ceil(n**(0.5))
#i range from 2 to 10    
    for i in range(2,u+1):
#when n can be exactly divided by at least one integer from 2 to 10, the circulation will keep on
#when n can't be exactly divided by any integer from 2 to 10, the circulation break
        if n%i == 0:
            p=False
     
print(n)

