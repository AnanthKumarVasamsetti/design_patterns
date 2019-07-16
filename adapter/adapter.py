"""
Adapter: This pattern facilitates communication between two existing systems by providing a compatible
         interface.

Example: In the following example there are two coffee machines old and new. The new coffee machine has a
         touchscreen but the old doesn't, we will be having an adapter that will be implementing operations of old
         coffee machine from touchscreen.
"""
# This is the old machine which has the two functionalities
class OldCoffeeMachine:
    def __init__(self, *args, **kwargs):
        return None
    
    def dispenseCappuccino(self):
        return "Cappuccino from old coffee machine"
    
    def dispenseEspresso(self):
        return "Espresso from old coffee machine"

# This is the new machine which contains touchscreen controls
class NewCoffeeMachine:
    def __init__(self, *args, **kwargs):
        return None

    def touchscreenDispenseCappuccino(self):
        return "Cappuccino from new coffee machine"
    
    def touchscreenDispenseEspresso(self):
        return "Espresso from new coffee machine"


# Adapter makes sure that there is compatible interface between the two coffee machines
class Adapter:
    def __init__(self, obj, **adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)   # As you can see here we are not updating the object __dict__ but updating the adapter's __dict__

    def getOriginalDict(self):
        return self.obj.__dict__

def main():
    oldMachine = OldCoffeeMachine()
    # Getting an adapter instance of old coffee machine with new interface
    oldMachineWithNewInterface = Adapter(oldMachine, touchscreenDispenseCappuccino=oldMachine.dispenseCappuccino)
    # Here the adapter acts as a wrapper upon the old machine
    # Call the old coffee machine with new interface
    print(oldMachineWithNewInterface.touchscreenDispenseCappuccino())

if __name__ == "__main__":
    main()
    