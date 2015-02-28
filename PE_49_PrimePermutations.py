## Author: James Norcross
## Date: 2/27/15
## Description: Finds 3 4-digit primes which have following properties
##      - they are an increasing sequence with fixed difference delta between elements
##      - they are all permutations of one another

from math import sqrt

## a prime sieve function
def makePrimeSieve(max):
    sieve = []
    
    ## initialize to true
    for i in range(max):
        sieve.append(True)
        
    ## make sieve
    sieve[0] = False
    sieve[1] = False
    sieve[2] = True
    
    imax = int(sqrt(max)) + 1
    
    for i in range(2,imax):
        if(sieve[i]):
            for j in range(2*i, max, i):
                sieve[j] = False

    return sieve

def isPermutation(n1, n2):
    list1 = list(str(n1))
    list2 = list(str(n2))
    if(len(list1) != len(list2)):
        return False
    for i in list1:
        if(i not in list2):
            return False
    for i in list2:
        if(i not in list1):
            return False
    return True

isPrime = makePrimeSieve(10000)

for p in range(1234, 9878):
    if(isPrime[p]):
        for delta in range(1, (9878-p)/2):
            p2 = p + delta
            if(isPrime[p2] and isPermutation(p, p2)):
                p3 = p2 + delta
                if(isPrime[p3] and isPermutation(p, p3)):
                    print "The answer is " + str(p) + str(p2) + str(p3)
                    break



        
