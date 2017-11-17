'''
Created on Oct 29, 2017
Pascal triangle
n<10 
n is user input
        1
       1 1
      1 * 1
     1 * * 1
    1 * * * 1  
@author: Akash
'''

n=int(input("Enter number of rows\n"))
for i in range(n):
    #if i!=1:
        print(" " *(n-i-1),end='')
        for j in range(i+1):
            if j==0 or j==i:
                print('1',end=' ')
            else:
                print('*',end=' ')
        print('\n',end='')