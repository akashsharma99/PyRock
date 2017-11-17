'''
Created on Oct 28, 2017
@author: Akash
*
**
***
**** n=4
'''
n=int(input("Enter size\n"))
for i in range(n):
    for x in range(i+1):
        print("*",end="")
    print("\n",end="")