'''to find grade according to the given system
90-100--->O
80-89---->E
70-79---->A
else ---->F'''
n=float(input("Enter marks of the student\n"))
if n>100 or n<0:
    print("Marks should be in range 0 to 100")
elif n>=90 and n<=100:
    print("O grade")
elif n>=80 and n<=89:
    print("E grade")
elif n>=70 and n<=79:
    print("A grade")
else:
    print("F grade\nSorry you have failed the examination :-(")