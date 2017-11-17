'''
Created on Oct 29, 2017
Pascal triangle
n<10 
n is user input
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1  
@author: Akash
'''

n=int(input("Enter number of rows\n"))
for i in range(n):
    print("  " *(n-i),end='')
    for j in range(i+1):
        if i==0 or j==0:
            co=1
        else:
            co=co*(i-j+1)//j
        if co<10:
            print('  ',end=' ')
        elif co<100:
            print(' ',end=' ')
        else:
            print(' ',end='')    
        print(co,end='')
    print('\n',end='')