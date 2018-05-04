import math
'''def isPrime(x):
    flag=0
    m=int(math.sqrt(x))
    for i in range(2,m+1):
        if(x%i==0):
            flag=1
            break
    if flag==0:
        return True
    else:
        return False

def pink():
    i=0
    n=int(input("Bhai ek number daal:\t"))
    k=int(n/2)
    for i in range(1,k+1):
        if(n%i==0 and isPrime(i)):
            print(i)
pink()'''
#def SieveOfEratosthenes(n):
n=int(input("Bhai ek number daal:\t"))
k=int(n/2)

# Create a boolean array "prime[0..n]" and initialize
#  all entries it as true. A value in prime[i] will
# finally be false if i is Not a prime, else true.
prime = [True for i in range(k+1)]
p = 2
while (p * p <= k):
     
    # If prime[p] is not changed, then it is a prime
    if (prime[p] == True):
         
        # Update all multiples of p
        for i in range(p * 2, k+1, p):
            prime[i] = False
    k += 1
k=int(n/2)
for i in range(1,k+1):
    if(n%i==0 and prime[i]):
        print(i)
