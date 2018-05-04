'''
Created on Feb 19, 2018

@author: akash
'''
class person:
    def name(self):
        print('name')
class teacher(person):
    def qualification(self):
        print('phd')
class hod(teacher):
    def experience(self):
        print('15 years')
h=hod()
h.name()
h.qualification()
h.experience()
