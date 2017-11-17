'''
Created on Oct 28, 2017

@author: akash
'''
n=int(input("Enter a number"))
copy=n
rev=0
while(copy!=0):
    d=copy%10
    copy=int(copy/10)
    rev=rev*10+d

if(rev==n):
    print("palindrome")
else:
    print("Not palindrome")