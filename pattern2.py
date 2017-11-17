'''
Created on Oct 28, 2017
@author: Akash
   1
  1 2
 1 2 3
1 2 3 4
n=4
'''
n=int(input("Enter size\n"))
for i in range(n):
    #space loop
    for sp in range(i,n-1):
        print(" ",end="")
    #number loop
    for j in range(i+1):
        print(j+1,"",end="")
    print("\n",end="")
