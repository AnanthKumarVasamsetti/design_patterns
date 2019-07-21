"""
Proxy: This is structural design pattern, it is something that acts as a simplified lightweight version
       of the original object. A proxy may perform the same tasks as an original object but may delegate
       requests to the original object to achieve them.

Example: The following is a warehouse example where the proxy class will take care of the order fulfillment
         by delegating the order to the respective warehouses. Here warehouses are designated to fulfill the order
         by delivery location, so warehouse1 delivers the orders for the addresses where the state name starts from [A-K]
         and warehouse2 delivers for the states whose name starts with [L-Z]. Proxy class will take care the delegation part 
         to which warehouse the order need to be sent.
"""


import abc

class Order:
    @abc.abstractclassmethod
    def fulfillOrder(self, order):
        pass

class Warehouse1(Order):
    def __init__(self):
        return

    def fulfillOrder(self, order):
        print("Order will be delivered to address: "+order["address"]+" by Warehouse 1")

class Warehouse2(Order):
    def __init__(self):
        return

    def fulfillOrder(self, order):
        print("Order will be delivered to address: "+order["address"]+" by Warehouse 2")

class Proxy(Order):
    def __init__(self):
        self.__warehouse1_obj__ = Warehouse1()
        self.__warehouse2_obj__ = Warehouse2()

    def fulfillOrder(self, order):


        if(order and order["address"]):
            if(ord(order["address"][0].lower()) in list(range(97,108))):
                self.__warehouse1_obj__.fulfillOrder(order)
            elif(ord(order["address"][0].lower()) in list(range(108,123))):
                self.__warehouse2_obj__.fulfillOrder(order)
            else:
                print("Enter valid address")

def main():
    orders = [
                {"item": "Groceries", "address": "Allahabad"},
                {"item": "Medicens", "address": "Surat"},
                {"item": "Electronics", "address": "Mumbai"},
                {"item": "Health and fitness", "address": "Delhi"}
            ]
    
    proxy = Proxy()
    
    for order in orders:
        proxy.fulfillOrder(order)

if __name__ == "__main__":
    main()