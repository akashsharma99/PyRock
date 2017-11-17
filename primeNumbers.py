'''
Created on Oct 27, 2017
@author: Akash
To print all the prime nubers between 1 to 100
Using Sieve of Eratosthenes:-

1.Created a boolean array with all elements initialised as true.
2.starting from 2 changed the state of all 
  multiples of 2 with False.
3.then starting from the next true position (i.e 3) 
  and changing it's multiples state to false.
4.Repeat step 3 till no further unchanged positions 
  left higher than the current number
'''
n=int(input("Enter limit\n"))
prime=[True for i in range(n+1)]#initialising array prime with True
p=2
while(p*p<=n):
    if(prime[p]==True):
        x=p*2
        while(x<=n):
            prime[x]=False
            x+=p;
    p+=1
# printing the prime numbers
i=2
while(i<=n):
    if(prime[i]==True):
        print(i,end=" ")
    i+=1