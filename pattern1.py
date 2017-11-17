'''
Created on Oct 27, 2017
@author:Akash
   *
  * *
 * * * n=3
  * *
   *
'''
n=int(input("Enter width\n"))
#for upper triangle
i=0
for i in range(n):
    #space loop for upper triangle
    for sp in range(i,n-1):
        print(" ",end="")
    #loop for * printing
    for j in range(i+1):
        print("* ",end="")
    print("\n",end="")
#for lower triangle
for i in range(n-1):
    #space loop
    for sp in range(i+1):
        print(" ",end="")
    #loop for * printing
    for j in range(i,n-1):
        print("* ",end="")
    print("\n",end="")