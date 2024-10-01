#from item import Item
#from phone import Phone
from keyboard import KeyBoard 

#Item.instantiate_from_csv()

#print(Item.all)

#item1 = Item("MyItem",750)
#item2 = Item("MyItem",850)
#item3 = Phone("jscPhone",1000,3)
item4 = KeyBoard("jscKeyBoard",1000,3)

'''
# Setting an Attribute
item1.name = "OtherItem"
item2.name = "OtherItemmm"

# Getting an Attribute
print(item1.name)
print(item1.read_only_name)

print(item1.price)

# Inheritance
item1.apply_increment(0.2)
item1.apply_discount()
print(item1.price)

item3.apply_increment(0.2)
print(item3.price)

# Polymorphism
item3.apply_discount()
print(item3.price)
'''
item4.apply_discount()
print(item4.price)
