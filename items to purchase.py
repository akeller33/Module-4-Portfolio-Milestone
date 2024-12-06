# Andrew Keller
# 12/6/2024

class ItemToPurchase:

    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.item_price * self.item_quantity:.2f}')



item1 = ItemToPurchase()
item1.item_name = input('Enter the name of the item. ')
item1.item_price = float(input('Enter the price of the item. '))
item1.item_quantity = int(input(' Enter the quantity to purchase. '))

item2 = ItemToPurchase()
item2.item_name = input('Enter the name of the item. ')
item2.item_price = float(input('Enter the price of the item. '))
item2.item_quantity = int(input(' Enter the quantity to purchase. '))

total = (item1.item_price*item1.item_quantity) + (item2.item_price*item2.item_quantity)

print('      TOTAL COST')
item1.print_item_cost()
item2.print_item_cost()
print(f'      Total: ${total:.2f}')
