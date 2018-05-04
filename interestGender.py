'''
Created on Dec 10, 2017

@author: akash
'''
gender=input("Enter gender 'male' or 'female'\n")
age=int(input("Enter age in years\n"))
if gender=='male':
    if age>=1 and age<=60:
        print("9.2%")
    elif age>=61 and age<=120:
        print("8.3%")
    else:
        print("age not valid")
elif gender=='female':
    if age>=1 and age<=58:
        print("8.2%")
    elif age>=59 and age<=120:
        print("7.6%")
    else:
        print("Age not valid")
else:
    print("gender not valid")