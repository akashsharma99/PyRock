'''
Created on Feb 18, 2018

@author: akash
'''

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self.age)
class teacher(person):
    def __init__(self,name,age,exp):
        person.__init__(self,name,age)
        self.exp=exp
    def displaydata(self):
        person.display(self)
        print(self.exp)
class student(person):
    def __init__(self,name,age,marks):
        person.__init__(self,name,age)
        self.marks=marks
    def displaydata(self):
        person.display(self)
        print(self.marks)
t=teacher('sir',33,3000)
t.displaydata()
s=student('arnab',22,90)
s.displaydata()
