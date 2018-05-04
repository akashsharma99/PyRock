'''
Created on Feb 18, 2018

@author:akash
'''
class abc:
    """hello world this is the 
documentation of class abc"""
    #'''hello world'''
    #__doc__='hello world'
    def __init__(self,var1,var2):
        self.var1=var1
        '''hello world'''
        self.var2=var2
    def display(self):
        print(self.var1)
        print(self.var2)
    
obj=abc(10,12.21)
obj.display()
print(obj.__dict__)
print(obj.__doc__)
print(obj.__module__)
print(abc.__name__)
print(abc.__bases__)