'''
Created on Feb 18, 2018

@author: akash
'''
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    @classmethod
    def square(cls,side):
        return cls(side,side)
    #def hello(cls,side):
    #    return cls(side,side)
#s=Rectangle.hello(10)
s=Rectangle.square(10)
print(s.area())