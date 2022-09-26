class car():
    def __init__(self,modelname,year,price):
        self.modelname = modelname
        self.year = year
        self.price = price

    def price_inc(self):
        self.price = int (self.price*1.15)

# Inheritance
class SuperCar(car):
    def __init__(self,modelname,year,price,cc):
        super.__init__(modelname,year,price)
        self.cc = cc

honda = SuperCar('city',2017,100000,1500)
tata = car('Bolt',2016,600000)

#honda.__dict__ function
print(tata.price)
honda.price_inc()
print(honda)  
#print(help(honda))



