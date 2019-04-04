import math
fact=[]
def factor(num):
    for i in range(1,num+1):
        if num%i ==0:
            fact.append(i)
    print(fact)

def pythagorus(x,y):
    hyp=math.sqrt(x**2+y**2)
    print(hyp)

if __name__=="__main__":
    factor(25)
    pythagorus(10,5)

