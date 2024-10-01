import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self,name: str,price: float,quantity=0): # Magic Method,Dunder Method
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity>= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        
        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all.append(self)
        
    # Encapsulation    
    @property
    def price(self):
        return self.__price
    
    def apply_discount(self):
        self.__price = self.__price * Item.pay_rate
    
    
    def apply_increment(self,increment_value):
        self.__price = self.__price + self.__price * increment_value 
        
    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        print("You are trying to get name")
        return self.__name 
    
    @name.setter  
    def name(self,value):
        print("You are trying to set name")
        if len(value) > 10:
            raise Exception("The name is too long!")
        self.__name = value
           
    def calculate_total_price(self):
        return self.__price * self.quantity
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )
    
    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # for i.e: 5.0,10.0
        if isinstance(num,float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False
    
    @staticmethod
    def get_total_items():
        pass
                
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name},{self.__price},{self.quantity})"
    
    @property
    def read_only_name(self):
        return "Read Only Name"
    
    # Abstarction
    def __connect(self,smpt_server):
        pass
    
    def __prepare_body(self):
        return f"""
        Hello Someone.
        We have {self.name}{self.quantity} times.
        Regards,JimShapedCoding
        """
    
    def __send(self):
        pass
    
    def send_eamil(self):
        self.__connect()
        self.__prepare_body()
        self.__send()
        
        
'''    
item1 = Item("Phone",100,5)
item2 = Item("Laptop",1000,3)
item3 = Item("Tablet",100,1)
item4 = Item("Cable",10,5)
item5 = Item("Mouse",50,5)
item6 = Item("Keyboard",75,5)

print(item1.calculate_total_price())
print(item2.calculate_total_price())
print(item3.calculate_total_price())

print(Item.pay_rate)
print(item1.pay_rate)
print(item2.pay_rate)
print(item3.pay_rate)

print(Item.__dict__) # All the attributes for class level
print(item1.__dict__) # All the attributes for Instance level

item1.apply_discount()
print(item1.price)

item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)
'''
'''
item1 = Item("Phone",100,5)
item2 = Item("Laptop",1000,3)
item3 = Item("Tablet",100,1)
item4 = Item("Cable",10,5)
item5 = Item("Mouse",50,5)
item6 = Item("Keyboard",75,5)

print(Item.all)
for instance in Item.all:
    print(instance.name,instance.quantity,instance.price)


Item.instantiate_from_csv()
print(Item.all)

print(Item.is_integer(7.0))
'''
