# Assignment 11 dec 2022
'''
1. Write a class called BankAccount that has the following:
        • A field called name that stores the name of the account holder.
        • A field called amount that stores the amount of money in the account.
        • A field called interest_rate that stores the account’s interest rate (as a percentage).
        • A constructor that just sets the values of the three fields above.
        • A method called apply_interest() that takes no arguments and applies the interest to the
        account. It should just modify the amount field and not return anything. For instance, if the
        account has $1000 in it and the interest rate is 3%, then the amount variable should be changed
        to $1030 ($1000 + 3% interest).
        Then test the class, by creating a new BankAccount object for a user named Juan De Hattatime who
        has $1000 at 3% interest. Then do the following:
        • Use the apply_interest() method to apply the interest to the account.
        • Print out how much money is now in the account after applying the interest.
        • Change the account’s interest rate to 2%.
        • Use the apply_interest() method to apply the interest to the account again.
        • Print out how much money is now in the account after applying the interest again.
'''
class BankAccount:
    def __init__(self,name,balance,irate) -> None:
        self.name = name
        self.balance = balance
        self.rate =irate

    def apply_interest(self):
        self.balance = self.balance+(self.balance*self.rate/100)


obj1 = BankAccount(name='Juan De Hattatime', balance=1000, irate=3)
obj1.apply_interest()
print('Balance in Account: $',obj1.balance)
obj1.irate = 2
obj1.apply_interest()
print('Balance in Account: $',obj1.balance)

'''
2.Write a class called Item that represents an item for sale. It should have the following:
    • Fields representing the name and price of the item
    • A constructor that sets those fields,
    • A __str__() method that returns a string containing the item name and price, with the price
    formatted to exactly 2 decimal places
    Test the class by creating a new item object and printing it out
'''

class Item:
    def __init__(self, item_name, item_price) -> None:
        self.name = item_name
        self.price = item_price
    
    def __str__(self) -> str:
        return f'item is {self.name}, and price is ${self.price:.2f}'

item1 = Item(item_name='ancient vase', item_price=99)
print(item1)

'''
3. Write a class called ShoppingCart that might be used in an online store. It should have the following:
      • A list of Item objects that represents the items in the shopping cart
      • A constructor that creates an empty list of items (the constructor should take no arguments except self)
      • A method called add() that takes a name and a price and adds an Item object with that name
      and price to the shopping cart
      • A method called total() that takes no arguments and returns the total cost of the items in the
      cart
      34
      • A method called remove_items() that takes an item name (a string) and removes any Item
      objects with that name from the shopping cart. It shouldn’t return anything.
      • A __str__() method that returns a string containing info on all the items in the shopping cart
      Then test out the shopping cart as follows: (1) create a shopping cart; (2) add several items to it; (3)
      print the cart’s total cost (using the total() method); (4) remove one of the items types; (5) print out
      the cart
'''
class ShoppingCart:
    items = []
    def __init__(self) -> None:
        self.item_list = []

    def add_item(self, item_name, item_price):
        self.item_list.append((item_name,item_price))

    def total(self):
        t = 0
        for i in self.item_list:
            t += i[1]
        return f'Total cost of items:${t:.2f}'
        
    def remove_items(self,item_name):
        for index in range(len(self.item_list)):
            if self.item_list[index][0] == item_name:
                self.item_list.pop(index)
                return None

    def __str__(self) -> str:
        print('Your shopping cart has:')
        for item in self.item_list:
            print(item[0], 'worth of $',item[1])
        return 'Thank You! for Shopping with us'

kshi = ShoppingCart()
kshi.add_item(item_name='pen stand',item_price=49.99)
kshi.add_item(item_name='laptop case',item_price=499.99)
kshi.add_item(item_name='sling bag',item_price=1499.99)
kshi.add_item(item_name='pen drive',item_price=399.99)
print(kshi, '\n', kshi.total())
kshi.remove_items('sling bag')
print(kshi, '\n', kshi.total())

'''
4. Write a class called RestaurantCheck. It should have the following:
      • Fields called check_number, sales_tax_percent, subtotal, table_number, and server_name
      representing an identification for the check, the bill without tax added, the sales tax percentage,
      the table number, and the name of the server.
      • A constructor that sets the values of all four fields
      • A method called calculate_total that takes no arguments (besides self) and returns the total
      bill including sales tax.
      • A method called print_check that writes to a file called check###.txt, where ### is the check
      number and writes information about the check to that file, formatted like below:
      Check Number: 443
      Sales tax: 6.0%
      Subtotal: $23.14
      Total: $24.53
      Table Number: 17
      Server: Sonic the Hedgehog
      Test the class by creating a RestaurantCheck object and calling the print_check() method
'''

class RestaurantCheck:
    def __init__(self, check_number, sales_tax_percent, subtotal, table_number,server_name:str) -> None:
        self.c_num = check_number
        self.tax = sales_tax_percent
        self.sub_total = subtotal
        self.table_num = table_number
        self.server = server_name        

    def calculate_total(self):
        total = self.sub_total + self.sub_total * (self.tax/100)
        return total

    def print_check(self):
        with open(f'check{self.c_num}.txt','w', encoding='utf-8') as f:
            f.write(f'Check Number:{self.c_num}\nSale tax:{self.tax}%\nSubtotal:${self.sub_total}\nTotal:${self.calculate_total()}\nTable Number:{self.table_num}\nServer:{self.server}')

person1 = RestaurantCheck(599,17,1560,5,'Sonic the Hedgehog')
person1.print_check()

'''
5. Write a class called Ticket that has the following:
      • A field cost for the price of the ticket and a string field time for the start time of the event
      (assume times are in 24-hour format, like '18:35')
      • A constructor that sets those variables
      • A __str__() method that returns a string of the form Ticket(<cost>, <time>), where
      <cost> and <time> are replaced with the values of the cost and time fields.
      • A method called is_evening_time() that returns True or False, depending on whether the
      time falls in the range from 18:00 to 23:59.
      • A method called bulk_discount() that takes an integer n and returns the discount for buying n
      tickets. There should be a 10% discount for buying 5 to 9 tickets, and a 20% discount for buying
      10 or more. Otherwise, there is no discount. Return these percentages as integers.
      Test the class by creating a Ticket item, printing it, calling the is_evening_time() method, and
      calling the bulk_discount() method
'''
from datetime import time
class Ticket:
    def __init__(self, price:int, time:str) -> None:
        self.ticket_price = price
        self.event_time = time

    def is_evening_time(self):
        t = self.event_time
        t=t.split(':')
        time_obj = time(int(t[0]),int(t[1]))
        if time(18,0)<time_obj<time(23,59):
            return True
        else:
            return False
    
    def bulk_discount(self,n):
        if 5<=n<=9:
            return 10
        elif n>=10:
            return 20
        else:
            return None
    
    def __str__(self) -> str:
        return f'Ticket({self.ticket_price},{self.event_time})'

t1 = Ticket(price=50,time='15:30')
print('t1\n', t1)
t2 = Ticket(price=80, time='18:30')
print('t2\n', t2)
is_evening_show = t1.is_evening_time()
print('t1 is evening show?',is_evening_show)
is_evening_show = t2.is_evening_time()
print('t2 is evening show?',is_evening_show)
print('For 4 tickets is discount applied?', t1.bulk_discount(4))
print('For 12 tickets is discount applied?', t2.bulk_discount(12))
print('For 8 tickets is discount applied?', t1.bulk_discount(8))