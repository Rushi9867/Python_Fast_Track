from item import Item

class KeyBoard(Item):
    pay_rate = 0.9
    def __init__(self,name: str,price: float,quantity=0): # Magic Method,Dunder Method
        # Call to,super function to have access to all attributes / Methods
        super().__init__(
            name,price,quantity 
        )
        