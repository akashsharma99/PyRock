'''
Created on Oct 28, 2017
                     *
                    ***
                   *****
@author:Akash
'''
n=int(input("Enter number"))
i=1
for x in range(1,n+1):
    for sp in range(x,n):
        print("  ",end="")
    for j in range(i):
        print("* ",end="")
    i=i+2
    print("\n",end="")
    