'''
Created on Jan 21, 2018
sets,frozensets,dictionary,functions,documentations
@author: akash
'''

from math import factorial
#from testcall import mat,a
import testcall #this is not working
set1=set({2,4,5,3,2,4,5})
print(set1)
set1.add(9)
print(set1)

set1=frozenset({2,4,5,3,2,4,5})
print(set1)
#set1.add(9)
#print(set1)

tel={'jack':99,'sope':100,'hello':123}
tel['guide']=123
print(tel)
dictionary=dict([('hello',34),('papa',99)])
print(dictionary)

def function_name():
    '''this is the documentation of function_name()'''
def fun():
    pass#in python we cannot leave fuction empty it will show error so we write pass
print(function_name.__doc__)#double underscore before and after doc

def simple_addition(num1,num2):
    answer=num1+num2
    print('num1 is ',num1)
    return answer
print('sum = ',simple_addition(5,3))

#returning more than one values
def data():
    x=10
    yield x;
    x+=10
    yield x;
    yield 'abc';
j=0
list1=[]
for i in data():
    #list1.append(i)
    #j+=1
    print(i)

list1=list(data())
print(list1)

def f():
    
    global s
    print(s)#generates error
    s="Hello"#modifies global variable
    print(s)#using the global s
#global

s="Python is great"
f()
print(s)

#we can define a function inside a function
def fun_outer(strr):
    def fun_inner():
        return "welcome "
    return fun_inner()+strr

def display(name):
    return name

print(fun_outer(display("akash")))
#lambda are like prameterized macros in C
#   #define add(x,y) x+y
#    main()
#    {
#        int res=add(2,3);
#    }
multiply=lambda x,y: x*y
print(multiply(10,7))
#two factorial using library and then using recursion

print(factorial(5))
#recursion
def factorial(x):
    if(x==1):
        return 1
    else:
        return x*factorial(x-1)
print('factorial of 5 is = ',factorial(5))
#importing modules and using member fuctions and variables

print(testcall.hello(6),'variable in testcall = ',testcall.a)

#import cmath
a=4
b=5
z=complex(a,b)
print(z.real)
print(z.imag)
print(z)