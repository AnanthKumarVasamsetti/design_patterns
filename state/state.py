"""
State pattern: This behavioural pattern makes the objects to choose appropriate behaviour based on their current state, when the current
               state changes the behaviour can be altered.

Example: The following example is of vending machine which has the states like idleState, hasdollarState, outOfStockState. So depending upon
         it's respective state the appropriate operations are performed, where these operations can be same in all the states but functioning will
         be different.
"""

import abc

class VendingMachine:

    def __init__(self):
        self.amount = 0
        __instance = None
        self.items_list = {
            "Snickers": {
                "cost": 0.99,
                "quantity": 20
            },
            "Lays": {
            "cost": 0.60,
                "quantity": 40
            },
            "Twix": {
                "cost": 0.80,
                "quantity": 20,
            },
            "Butter finger": {
                "cost": 0.40,
                "quantity": 40,
            },
            "Baby ruth": {
                "cost": 0.40,
                "quantity": 40,
            }
        }
    
    def add_money(self, money_inserted):
        self.amount = self.amount + money_inserted
        
    def get_has_dollar_state(self):
        return HasdollarState()
    
    def set_state(self, state_object):
        self.state = state_object
    
    def eject_money(self):
        return self.amount
    
    def calculate_change(self, item_cost):
        if item_cost > self.amount:
            print("Item price is more than the inserted amount")
        else:
            self.amount = self.amount - item_cost
            print("Dispensing Item \n Remaining amount: ", self.amount)

class State:
    
    @abc.abstractclassmethod
    def insert_dollar(self, vending_machine_object, money_inserted):
        pass
    
    @abc.abstractclassmethod
    def dispense(self, vending_machine_object):
        pass
    
    @abc.abstractclassmethod
    def eject_money(self, vending_machine_object):
        pass

class IdleState(State):
    
    def __init__(self):
        pass
    
    def insert_dollar(self, vending_machine_object, money_inserted):
        print("Inserting ",money_inserted," into the vending machine")
        vending_machine_object.add_money(money_inserted)
        vending_machine_object.set_state(vending_machine_object.get_has_dollar_state())
    
    def dispense(self, vending_machine_object):
        print("Payment required")
    
    def eject_money(self, vending_machine_object):
        print("No money to return")

class HasdollarState(State):

    def __init__(self):
        pass
    
    def insert_dollar(self, vending_machine_object):
        print("Already has one dollar")
    
    def dispense(self, vending_machine_object):
        print("Dispensing selected item")
        vending_machine_object.set_state(vending_machine_object.get_idle_state())
    
    def eject_money(self, vending_machine_object):
        print("Returning money")
        vending_machine_object.set_state(vending_machine_object.get_idle_state())

if __name__ == "__main__":

    vending_machine_obj = VendingMachine()
    vending_machine_obj.add_money(10)
