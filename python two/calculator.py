class calculator:

    def __init__(self):
        self.sum=0
        self.ml=1
        self.sb=0
        
    def add(self,*args):
        print(sum(args))
    def div(self,n,d):
        print(n/d)
    def mul(self,*args):
        for i in args:
            self.ml*=i
        print(self.ml)


if __name__=="__main__":
    cal=calculator()
    cal.add(1,2,3,4)
    cal.mul(2,4,5)
    cal.div(8,2)
    cal.add(500,-400)
    