'''
Created on Feb 17, 2018

@author: akash
'''
class Test:
    a="poop"
    '''def __init__(self):
        self.name="empty"  '''
    def __init__(self,name,v2):#double underscore!init is a constructor
        self.name=name
        self.__v2=v2#double underscore means private
        self._v1=v2#single underscore is protected
    def fun(self):#by default a reference is passed during function call so self has to be given
        a="hello"
        print(a)
        print(self.a)
obj=Test("akash",56)
obj.fun()
print(obj.a)
print(obj.name)
'''print(obj.__v2) #wont work since __v2 is a private type variable'''
print(obj._Test__v2)#to access private data member outside class

print(getattr(obj,'name'))#get attribute
print(getattr(obj,'_Test__v2'))
print(hasattr(obj,'Test_v1'))


class student:
    def __init__(self,a):
        self.__a=a;
        self.cgpa=0;
    def calculate(self):
        tot=0;
        for i in range(5):
            tot=tot+self.__a[i]
        self.cgpa=tot/5
mark=[]        
for i in range(5):
    mark.append(int(input()))
print(mark)
obj=student(mark)
obj.calculate()
print(obj.cgpa)