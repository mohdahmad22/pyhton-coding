class Laptop:

    def __init__(self,brand,year,ram,processor):
        self.brand=brand
        self.yr=year
        self.ram=ram
        self.cpu=processor


    def show(self):
        print("laptop details")
        print(self.brand)
        print(self.yr)
        print(self.ram)
        print(self.cpu)


if __name__=="__main__":
    l=Laptop('dell','2017','4gb','i3')
    n=Laptop('msi','2017','16gb','i7')
    l.show()
    n.show()


        
        
