'''
Created on Feb 19, 2018

@author:
'''
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
    def mooo(self):
        print('lello')
class Human(Animal):
    def move(self):
        print("I can walk")
class Snake(Animal):
    def move(self):
        print("I can crawl")
h1=Human()
h1.move()
s1=Snake()
s1.move()
obj=Animal()