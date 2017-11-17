n=int(input("Enter a limit\n"))
x=0
y=1
z=1
if(n<=0):
    print("Wrong input: enter a positive number")
else:
    for i in range(1,n+1):
        if i==1:
            print(0)
        elif i==2:
            print(1)
        else:
            z=x+y
            print(z)
            x=y
            y=z
