from item import Item
from phone import Phone
from keyboard import KeyBoard 

#Item.instantiate_from_csv()

#print(Item.all)
'''
item1 = Item("MyItem",750)

# Setting an Attribute
item1.name = "OtherItem"

# Getting an Attribute
print(item1.name)
print()
print(item1.read_only_name)
print()
print(item1.price)
# Inheritance
print("***Inheritance***")
item1.apply_increment(0.2)
print(item1.price)
print("***Apply_discount***")
item1.apply_discount()
print(item1.price)
'''

'''
item2 = Item("MyItem",850)

# Setting an Attribute

item2.name = "OtherItemmm"
print(item2.name)
'''

'''
item3 = Phone("jscPhone",1000,3)

item3.apply_increment(0.2)
print(item3.price)

# Polymorphism
print("*** Polymorphism ***")
item3.apply_discount()
print(item3.price)
'''

item4 = KeyBoard("jscKeyBoard",1000,3)
item4.apply_discount()
print(item4.price)
