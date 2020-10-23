
#declaring a class for items
class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def updateStock(self, stock):
        self.stock = stock

    def buyFromStock(self):
        if self.stock == 0:
            pass
        self.stock -= 1
#declaring a class for the vending machine 
class VendingMachine:
    def __init__(self):
        self.amount = 0
        self.items = [] #array that will hold the items

    def addItem(self, item):
        self.items.append(item) #appending the items to the array

    def showItems(self):
        print('\nitems available \n')
        for item in self.items:      
            if item.stock == 0:
                self.items.remove(item)
        for item in self.items:
            print(item.name, item.price)

#adding cash into the vending machine(user input)
    def addCash(self, money):
        self.amount = self.amount + money
#check to see if money is suffecciant for item 
    def buyItem(self, item):
        if self.amount < item.price:
            print('You can\'t but this item. Insert more coins.')
        else:
            self.amount -= item.price
            item.buyFromStock()
            print('You got ' +item.name)
            print('Cash remaining: ' + str(self.amount))
#check to see if item is in stock
    def containsItem(self, wanted):
        ret = False
        for item in self.items:
            if item.name == wanted:
                ret = True
                break
        return ret

    def getItem(self, wanted):
        ret = None
        for item in self.items:
            if item.name == wanted:
                ret = item
                break
        return ret
#string input to ask user to enter and store money into machine
    def insertAmountForItem(self, item):
        price = item.price
        while self.amount < price:
                self.amount = self.amount + float(input('insert ' + str(price - self.amount) + ': '))
#if user leaves with money still in vending machine it should be refunded
    def checkRefund(self):
        if self.amount > 0:
            print(self.amount + " refunded.")
            self.amount = 0

        print('Thank you, have a nice day!\n')


def vendingmachine():
#declaring all the items, the prices, and adding them into the vendding machine
    machine = VendingMachine()
    item1 = Item('skittles',  1.5,  2)#shows the item name, the price, and the stock
    item2 = Item('coke', 1.75,  1)
    item3 = Item('ruffles',  2.0,  3)
    item4 = Item('popcorn',  0.50, 1)
    item5 = Item('gum',0.75,  3)
    machine.addItem(item1)
    machine.addItem(item2)
    machine.addItem(item3)
    machine.addItem(item4)
    machine.addItem(item5)

    print('Welcome to the vending machine!\n')
#while loop to ask user if they want to continue buying or if they wish to leave the vending machine
    continueToBuy = True
    while continueToBuy == True:
        machine.showItems()
        selected = input('select item: ')
        if machine.containsItem(selected):
            item = machine.getItem(selected)

            machine.insertAmountForItem(item)
            machine.buyItem(item)

            a = input('buy something else? (y/n): ')
            if a == 'n':
                continueToBuy = False
                machine.checkRefund()
            else:
                continue

        else:
            print('Item not available. Select another item.')
            continue

vendingmachine()
