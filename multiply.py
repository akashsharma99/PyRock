'''
Created on Dec 9, 2017

@author:Akash
'''
import time
n=int(input("number"))

t1=time.time()
print(n+(n<<3))
t2=time.time()
print(time.time()-t1)