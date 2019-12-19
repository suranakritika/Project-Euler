# Code

#!/bin/python3

import sys
import math 

def SieveOfEratosthenes(n): 
    m = pow(math.floor(math.sqrt(n))+1,2)
    prime = [True for i in range(0,n+1)]     
    p = 2
    while(p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * 2, n+1, p): 
                prime[i] = False
        p += 1
    for p in range(2, n): 
        if prime[p]: 
            l.append(p)
    return l

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    l=[]
    l=SieveOfEratosthenes(n+1)
    k=1
    for i in l:
        j=1
        while(i**(j+1) <= n):
            j+=1
        k*=i**j
    print(k)
    
