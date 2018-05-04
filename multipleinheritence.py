'''
Created on Feb 18, 2018

@author: akash
'''
class base1:
    def __init__(self):
        #super(base1,self).__init__()
        #super().__init__()
        print('base1')
class base2:
    def __init__(self):
        #super(base2,self).__init__()
        #super().__init__()
        print('base2')
class derived(base2,base1):
    def __init__(self):
        super(derived,self).__init__()
        #super().__init__()
        print('derived')
d=derived()