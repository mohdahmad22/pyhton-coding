class emp:
    dept='accounts'

    def show(self):
        print('the employee class')  #self is mandatory for defining fucnction inside python classes
    def show2(self):
        print('second function')


if __name__=='__main__':
    e1=emp()
    print(e1)
    print(type(e1))
    e1.show()
    e1.show2()
