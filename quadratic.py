import math
   

def quadfor (numa, numb, numc): 
    if numa==0: 
        print("error! You can't divide by 0 my friend ")
        quit()
    x=numa*numc
    y=x*4
    z=numb**2
    m=z-y
    if m<0:  
        print("oh no")
    else: 
        l=math.sqrt(m)
        d=-numb
        r1=d+l
        r2=d-l
        o=2*numa
        k1=r1/o
        k2=r2/o
        oppk1=-k1
        oppk2=-k2
        if k1>0 and k2>0: 
            print("The equation of the quadratic is " + str(a) + "(x " + "+ " + str(oppk1) + " )" "(x " + "+ " + str(oppk2) + " )" )
        return (k1,k2)



a = int(input('Enter number a:\n'))
b = int(input('Enter number b:\n'))
c = int(input('Enter number c:\n'))
d = quadfor(a,b,c)
print(d)

