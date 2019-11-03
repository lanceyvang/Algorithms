class Line:
    
    def __init__(self, coor1, coor2):
        self.rise = max(coor1[1], coor2[1]) - min(coor1[1], coor2[1]) 
        self.run = max(coor1[0], coor2[0]) - min(coor1[0], coor2[0]) 

    def distance(self):
        return (self.rise**2 + self.run**2) ** (1/2)

    def slope(self):
        return self.rise / self.run

l = Line((3,2),(8,10))
# print(l.rise, l.run, l.slope(), l.distance())
# print(l.distance())

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None # the pointer initially points to nothing

def traverse(self):
    node = self # start from the head node
    while node != None:
        print(node.val) # access the node value
        node = node.next # move on to the next node

class Cylinder:
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.pi * self.radius**2 * self.height

    def surface_area(self):
        return 2*self.pi*self.radius*self.height + 2*self.pi*self.radius**2
    
c = Cylinder(2,3)

# print(c.volume())
# print(c.surface_area())

class Bank_Account:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner: {self.owner}\nAccount balance: {self.balance}'

    def deposit(self, amount=0):
        self.balance += amount
        print(f'${amount} deposit accepted, your current balance is now ${self.balance}')

    def withdraw(self, amount=0):

        if amount > self.balance:
            print('Funds Unavailable!')
        else:
            self.balance -= amount
            print(f'${amount} withdrawal accepted, your current balance is now ${self.balance}')

b = Bank_Account('Yang', 500)

