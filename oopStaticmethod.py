'''
Created on Feb 18, 2018

@author:akash
'''
class myclass:
    x=1
    @staticmethod
    def square(self,x):
        print(self**2)
#obj=myclass()
#obj.square(10)
myclass.square(3,2)
print(myclass.x)