'''
Created on Feb 17, 2018

@author: akash
'''
class student:
    def __init__(self):
        #self.__a=a;
        self.cgpa=0;
    def calculate(self):
        tot=0;
        for i in range(5):
            if self.__a[i]==10:
                self.__a[i]=9
            tot=tot+self.__a[i]+1
        self.cgpa=tot/5
mark=[]
print("Enter marks in five subjects")        
for i in range(5):
    mark.append(int(int(input())/10))
print("The grade points in each subject are")
print(mark)
obj=student()
setattr(obj,'_student__a',mark)
obj.calculate()
print("CGPA is =",end='')
print(obj.cgpa)