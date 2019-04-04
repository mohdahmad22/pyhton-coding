import math
def adder(a=1,b=0,c=3,d=30):
    return a+b+c+d
def eq1(a,b):
    return a**2+b**2+2*a*b
def pythagorus(p,b):
    h=math.sqrt(p**2+b**2)
    h=round(h,4)
    return h,p,b
def patrn(sym='*',size=9):
    for i in range(size):
        print(sym*i,end=' ')
        print('\n')
        
    
if __name__=="__main__":
    out=eq1(12,13)

    #hyp,p,b=pythagorus(10,5)
    #print("result 1:",out)
    print(adder(1,3,4))
    print(adder(1,3,4,5))
    print(adder(d=12,b=10))
    patrn('#',5)
    patrn('*',10)
    patrn('&',15)
    patrn('(',20)
    
    

