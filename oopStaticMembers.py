'''
Created on Feb 18, 2018

@author: akash
'''
class CSStudent:
    stream='cse'#by default becomes static. class variable
    def __init__(self,name,roll):
        self.name=name#not static instance variable
        self.roll=roll
a=CSStudent('geek',1)
b=CSStudent(5,2)#look here objects of same class but different argument types
print(a.stream)
print(b.stream)
a.stream='a me change kiya'
print(a.stream)
print(b.stream)
print(a.name)
print(b.name)
print(a.roll)
print(b.roll)
print(CSStudent.stream)
#print(CSStudent.name)#throws error since name is not static        