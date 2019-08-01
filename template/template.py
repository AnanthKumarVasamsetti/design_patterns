"""
Template: It is a behavioural design pattern which deals with the algorithm's steps generally, deferring the implementation
          of some steps to subclasses.
Example: The following example is concerned about the preparation of pasta. In this preparation there are some steps which 
         are common of any variety of preparation so we shall make them as private and the rest of the deferring steps are given
         access to it's subclasses.
"""
import abc

class PastaTemplate:

    def __init__(self):
        return
    
    def __boil_water(self):
        print("Water is boiling")
    
    def __cook_pasta(self):
        print("Pasta is cooking")
    
    def __drain_and_plate(self):
        print("Draining the pasta and adding to the plate")
    
    @abc.abstractclassmethod
    def add_pasta(self):
        pass

    @abc.abstractclassmethod
    def add_sauce(self):
        pass

    @abc.abstractclassmethod
    def add_protein(self):
        pass

    @abc.abstractclassmethod
    def add_garnish(self):
        pass
    
    def make_recipe(self):
        self.__boil_water()
        self.add_pasta()
        self.__cook_pasta()
        self.__drain_and_plate()
        self.add_sauce()
        self.add_protein()
        self.add_garnish()
    
class SpaghettiPasta(PastaTemplate):
    
    def add_pasta(self):
        print("Adding spaghetti pasta")
    
    def add_sauce(self):
        print("Adding red sauce")
    
    def add_protein(self):
        print("Adding meatballs")
    
    def add_garnish(self):
        print("Adding parsley")

class PenneAlfredo(PastaTemplate):

    def add_pasta(self):
        print("Adding penne pasta")
    
    def add_sauce(self):
        print("Adding white sauce")
    
    def add_protein(self):
        print("Adding pork")
    
    def add_garnish(self):
        print("Adding basil")

if __name__ == "__main__":
    while(True):
        selected = int(input("\nSelect one pasta kind \n1. Spaghetti \n2. Penne Alfredo\n"))
        if selected == 1:
            SpaghettiPasta().make_recipe()
        elif selected == 2:
            PenneAlfredo().make_recipe()
        else:
            print("Make correct selection")