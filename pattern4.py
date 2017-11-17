'''
Created on Oct 28, 2017
@author: Akash
1
12
123
1234
12345 n=5
'''
n=int(input("Enter a size\n"))
for i in range(n):
    for j in range(i+1):
        print(j+1,end="")
    print("\n",end="")