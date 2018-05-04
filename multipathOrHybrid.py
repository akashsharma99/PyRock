'''
Created on Feb 19, 2018

@author: akash
'''
'''class A:
    def printB1(self):
        print('a')
class B1(A):
    def printB1(self):
        print('b1')
class B2(A):
    def printB2(self):
        print('b2')
class C(B1,B2):
    def printC(self):
        print('c')
obj=C()
obj.printB1()
obj.printB1()
obj.printB2()
obj.printC()'''

class student:
    def name(self):
        print('name')
class academic(student):
    def score1(self):
        print('90')
class eca(student):
    def score2(self):
        print('80')
class result(academic,eca):
    def eligibility(self):
        self.score1()
        self.score2()
r=result()
r.eligibility()