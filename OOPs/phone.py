from item import Item

class Phone(Item):
    pay_rate = 0.5
    def __init__(self,name: str,price: float,quantity=0,broken_phones=0): # Magic Method,Dunder Method
        # Call to,super function to have access to all attributes / Methods
        super().__init__(
            name,price,quantity 
        )
        # Run validations to the received arguments
        assert broken_phones>= 0, f"Broken Phones {broken_phones} is not greater than or equal to zero!"
        
        # Assign to self object
        self.name = name
        self.__price = price
        self.quantity = quantity
        self.broken_phones = broken_phones
        
        # Actions to execute
        Phone.all.append(self)
       
    @property
    def price(self):
        return self.__price
    
    def apply_discount(self):
        self.__price = self.__price * Item.pay_rate
    
    
    def apply_increment(self,increment_value):
        self.__price = self.__price + self.__price * increment_value 

'''
phone1 = Phone("jscPhonev10",500,5,1)
print(phone1.calculate_total_price())
phone2 = Phone("jscPhonev20",700,5,1)
print(phone2.calculate_total_price())
'''
'''
print(Item.all)
print(Phone.all)
'''