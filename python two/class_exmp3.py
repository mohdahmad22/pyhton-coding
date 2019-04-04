class Pet:
    def __init__(self,name,age,color,type="dog"):
        self.name=name
        self.age=age
        self.color=color
        self.type=type

    def do_trick(self,trick='flip'):
        print(f"{self.name} is tryiing to {trick}")
    def eat(self,item='biscuit'):
        print(f"{self.name} eats a {item}")
    def speak(self,sound='bow bow'):
        print(f"{self.name} does {sound}")
    
if __name__=="__main__":
    dg=Pet('tommy','2','white')
    dg.do_trick()
    dg.eat('pizza')
    dg.speak()

    perry=Pet('perry',6,'sea green','platypus')
    perry.eat()
    perry.speak('grrr')
    perry.do_trick('flip')  


